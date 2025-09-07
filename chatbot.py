import pandas as pd
import numpy as np

# Load the data from the CSV file
df = pd.read_csv('Financial_Report.csv')

# Function to retrieve data based on the query
def financial_chatbot(company, year, query):
    
    # Check if the company exists in the dataset
    if company.lower() not in df['Company'].str.lower().unique():
        return f"Sorry, we don't have data for {company}."

    # Check if the year exists for the specified company
    available_years = df[df['Company'].str.lower() == company.lower()]['Year'].unique()
    if year not in available_years:
        return f"Sorry, we don't have data for {company} in {year}."

    # Filter the data for the specified company and year
    company_data = df[(df['Company'].str.lower() == company.lower()) & (df['Year'] == year)]
    
    # User queries
    if query == "total revenue":
        value = company_data['Total Revenue'].values[0]
        if pd.isna(value):
            return f"Sorry, we don't have total revenue for {company} in {year}."
        return f"The total revenue for {company} in {year} was {value} million."
    
    elif query == "net income":
        value = company_data['Net Income'].values[0]
        if pd.isna(value):
            return f"Sorry, we don't have net income for {company} in {year}."
        return f"The net income for {company} in {year} was {value} million."
    
    elif query == "total assets":
        value = company_data['Total Assets'].values[0]
        if pd.isna(value):
            return f"Sorry, we don't have total assets for {company} in {year}."
        return f"The total assets for {company} in {year} were {value} million."
    
    elif query == "total liabilities":
        value = company_data['Total Liabilities'].values[0]
        if pd.isna(value):
            return f"Sorry, we don't have total liabilities for {company} in {year}."
        return f"The total liabilities for {company} in {year} were {value} million."
    
    elif query == "cash flow":
        value = company_data['Cash Flow from Operating Activities'].values[0]
        if pd.isna(value):
            return f"Sorry, we don't have cash flow for {company} in {year}."
        return f"The cash flow from operating activities for {company} in {year} was {value} million."
    
    else:
        return "I'm not sure how to answer that. Can you try a different question?"


def main():
    print("Hi, Welcome to the Global Finance Corp. (GFC) AI Chatbot!")
    print("I can provide information about financial data of our client companeies.")
    
    while True:
        company = input("Which company's data do you want to know about? (Microsoft/Apple/Tesla): ").strip()
        
        # Check if the company exists in the dataset
        if company.lower() not in df['Company'].str.lower().unique():
            print(f"Sorry, we don't have data for {company}.")
            continue

        year = input("Which year? (2021/2022/2023): ").strip()

        # check if the year entered is valid
        try:
            year = int(year)
        except ValueError:
            print(f"Sorry, {year} is not a valid year.")
            continue

        available_years = df[df['Company'].str.lower() == company.lower()]['Year'].unique()
        if year not in available_years:
            print(f"Sorry, we don't have data for {company} in {year}.")
            continue

        query = input("What would you like to know? (total revenue, net income, total assets, total liabilities, cash flow): ").strip().lower()

        # the response based on user query
        print(financial_chatbot(company, year, query))

        cont = input("Do you want to ask something else? (yes/no): ").lower()
        # if cont != 'yes':
        if not cont.startswith('y'):
            break

if __name__ == "__main__":
    main()
