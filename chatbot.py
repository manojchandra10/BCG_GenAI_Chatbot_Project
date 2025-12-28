import pandas as pd
import re

class FinancialChatbot:
    def __init__(self, data_path):
        # Load data
        self.df = pd.read_csv(data_path)
        self.df['Company_Lower'] = self.df['Company'].str.lower()

    def extract_intent(self, user_input):
        """
        Parses the user string to find Company, Year, and Metric.
        """
        user_input = user_input.lower()
        
        # Identify Company
        company = None
        if "microsoft" in user_input:
            company = "Microsoft"
        elif "apple" in user_input:
            company = "Apple"
        elif "tesla" in user_input:
            company = "Tesla"
            
        # Identify Year
        year = None
        year_match = re.search(r'20[0-9]{2}', user_input)
        if year_match:
            year = int(year_match.group())
            
        # Identify Metric (Map keywords to column names)
        metric = None
        if "revenue" in user_input or "sales" in user_input:
            metric = "Total Revenue"
        elif "net income" in user_input or "profit" in user_input or "earnings" in user_input:
            metric = "Net Income"
        elif "asset" in user_input:
            metric = "Total Assets"
        elif "liabilities" in user_input or "debt" in user_input:
            metric = "Total Liabilities"
        elif "cash" in user_input or "flow" in user_input:
            metric = "Cash Flow from Operating Activities"
            
        return company, year, metric

    def get_response(self, user_input):
        company, year, metric = self.extract_intent(user_input)

        if not company:
            return "I can help with financial data for Microsoft, Apple, and Tesla. Which one are you asking about?"
        
        if not year:
            return "I found you are interested in " + str(company) + ", but I need a year (2021-2023) to give you specific data."
        
        if not metric:
            return "I have data for " + str(company) + " in " + str(year) + ", but I'm not sure what value you want. You can ask about Revenue, Net Income, Assets, Liabilities, or Cash Flow."

        # Retrieve Data
        try:
            row = self.df[(self.df['Company_Lower'] == company.lower()) & (self.df['Year'] == year)]
            
            if row.empty:
                return "Sorry, I don't have records for " + str(company) + " in " + str(year) + "."

            value = row[metric].values[0]
            
            formatted_value = format(value, ",.0f")
            return str(company) + "'s " + str(metric) + " in " + str(year) + " was $" + formatted_value + " million."
            
        except Exception as e:
            return "An unexpected error occurred while retrieving your data."

def main():
    # Initialize chatbot
    bot = FinancialChatbot('Financial_Report.csv')
    
    print("Global Finance Corp. (GFC) AI Chatbot")
    print("I can answer complex queries like: 'What was Tesla's profit in 2022?'")
    print("Type 'exit' or 'quit' to stop.")

    while True:
        user_input = input("\nYour Question: ").strip()
        
        if user_input.lower() in ['exit', 'quit', 'no', 'bye']:
            print("Goodbye! Have a great day.")
            break
            
        response = bot.get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()