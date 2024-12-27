import csv  
from datetime import datetime  

# Function to log an expense into the 'expenses.csv' file
def log_expense(amount, category, description):
    with open('expenses.csv', 'a', newline='') as file: 
        writer = csv.writer(file) 
        writer.writerow([datetime.now(), amount, category, description])  

# Function to generate and print a report of total expenses from the CSV file
def generate_report():
    with open('expenses.csv', 'r') as file:  
        reader = csv.reader(file) 
        total = 0  # Variable to store the sum of all expenses
        for row in reader:  # Looping through each row in the CSV file
            total += float(row[1])  # Adding the expense amount (second column) to the total
            print(f'Total Expenses: ${total:.2f}')  # Printing the total expenses

# Logging a sample expense
log_expense(150, 'Appliances', 'Refrigerator and Washing Machine')

# Generating and displaying the report of total expenses
generate_report()
