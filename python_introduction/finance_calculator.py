# finance_calculator.py

# Prompt the user to input their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user to input their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project the annual savings with a 5% interest rate
annual_savings = monthly_savings * 12
annual_savings_with_interest = annual_savings + (annual_savings * 0.05)

# Display the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings_with_interest:.2f}.")
