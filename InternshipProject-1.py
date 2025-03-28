import math
import pandas as pd
import numpy as np

# Mortgage Calculator
def mortgage_calculator(P, annual_rate, years):
    r = annual_rate / 100 / 12
    n = years * 12
    M = P * r * math.pow(1 + r, n) / (math.pow(1 + r, n) - 1)
    return round(M, 2)

# Investment Return Calculator
def investment_calculator(P, rate, years):
    FV = P * math.pow(1 + rate / 100, years)
    return round(FV, 2)

# Savings Goal Calculator
def savings_goal_calculator(goal, rate, years):
    r = rate / 100 / 12
    n = years * 12
    PMT = goal * r / (math.pow(1 + r, n) - 1)
    return round(PMT, 2)

# Income Tax Calculator (Updated for 2025)
def income_tax_calculator(income, deductions):
    taxable_income = income - deductions - 75000
    tax = 0
    if taxable_income <= 400000:
        tax = 0
    elif taxable_income <= 800000:
        tax = (taxable_income - 400000) * 0.05
    elif taxable_income <= 1200000:
        tax = (taxable_income - 800000) * 0.10 + 20000
    elif taxable_income <= 1600000:
        tax = (taxable_income - 1200000) * 0.15 + 60000
    elif taxable_income <= 2000000:
        tax = (taxable_income - 1600000) * 0.20 + 120000
    elif taxable_income <= 2400000:
        tax = (taxable_income - 2000000) * 0.25 + 200000
    else:
        tax = (taxable_income - 2400000) * 0.30 + 300000
    return round(tax, 2)

# Bulk Calculation using Pandas
def bulk_calculations():
    input_file = input("Enter input CSV file path: ")
    output_file = input("Enter output CSV file path: ")

    df = pd.read_csv(input_file)
    df['Monthly Mortgage'] = df.apply(lambda row: mortgage_calculator(row['Loan Amount'], row['Annual Rate'], row['Loan Term']), axis=1)
    df['Investment Value'] = df.apply(lambda row: investment_calculator(row['Initial Investment'], row['Return Rate'], row['Investment Period']), axis=1)
    df['Monthly Savings'] = df.apply(lambda row: savings_goal_calculator(row['Savings Goal'], row['Return Rate'], row['Time Frame']), axis=1)
    df['Tax Liability'] = df.apply(lambda row: income_tax_calculator(row['Income'], row['Deductions']), axis=1)

    df.to_csv(output_file, index=False)
    print("Bulk calculations completed and saved to", output_file)

# Main Function with Menu
def main():
    while True:
        print("\nFinancial Planning Toolkit")
        print("1. Mortgage Calculator")
        print("2. Investment Return Calculator")
        print("3. Savings Goal Calculator")
        print("4. Income Tax Calculator")
        print("5. Bulk Calculations")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            P = float(input("Enter loan amount (in INR): "))
            rate = float(input("Enter annual interest rate (%): "))
            years = int(input("Enter loan term (in years): "))
            print(f"Monthly mortgage payment: ₹{mortgage_calculator(P, rate, years)}")
        elif choice == '2':
            P = float(input("Enter initial investment amount (in INR): "))
            rate = float(input("Enter expected annual return rate (%): "))
            years = int(input("Enter investment period (in years): "))
            print(f"Future value of investment: ₹{investment_calculator(P, rate, years)}")
        elif choice == '3':
            goal = float(input("Enter savings goal amount (in INR): "))
            rate = float(input("Enter expected annual return rate (%): "))
            years = int(input("Enter time frame (in years): "))
            print(f"Monthly savings needed: ₹{savings_goal_calculator(goal, rate, years)}")
        elif choice == '4':
            income = float(input("Enter your annual income (in INR): "))
            deductions = float(input("Enter your total deductions (in INR): "))
            print(f"Estimated tax liability: ₹{income_tax_calculator(income, deductions)}")
        elif choice == '5':
            bulk_calculations()
        elif choice == '6':
            print("Exiting...thanks for using!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
