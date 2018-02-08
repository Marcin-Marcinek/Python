#!/usr/bin/python3
print("Debt calculator")
debt = float(input("Ammount of debt (in PLN):"))
daily_interest = float(input("Late fees per day: "))
days = int(input("Number of days since paydate: "))
total_debt = debt + daily_interest * days
print("Total ammount of debt: ", total_debt, "PLN")
