#!/usr/bin/env python3.10

import math
from tarfile import REGULAR_TYPES
  
print(f"Welcome this system will print your weekly paycheck.\n"
      f"Our system only accepts real numbers as a valid input.\n"
      f"The sky is the limit for your pay rate!!!\n"
      f"We do know that you can't work more hours than there are in a week, so no funny business!!\n")

# Verify valid input for name of employee
while True:
    employee_name = str(input("Enter the employee's name: "))
    if employee_name.isalpha() != True:
        print("Please enter a valid name.")
        continue
    break

# Verify valid input for hourly pay rate
while True:  
    try:      
        hourly_rate = float(input("Enter your pay rate: "))
    except ValueError:
        print("Please enter a valid pay rate.")
        continue
    break

# Verify valid input for amount of hours worked
while True: 
    try:
        hours_worked = float(input("Enter amount of hours worked: "))
    except ValueError:
        print("Please enter a valid amount of hours worked.")
        continue
    if hours_worked <= 0:
        print("Please enter a valid amount of hours worked.")
    elif hours_worked > 168:
        print("Please enter a valid amount of hours worked.")
    else:
        break    

# Calculate Regular Pay 
def calculate_regular_pay():
    regular_pay = float(hourly_rate * hours_worked) 
    return round(regular_pay, 2)

# Calculate Overtime Pay
def calculate_overtime_pay():
    if hours_worked > 40:
        overtime_hours = float(hours_worked - 40)
        overtime_pay = float(overtime_hours * (hourly_rate * 1.5))
        return round(overtime_pay, 2)
    else:
        return int(0)

# Calculate Gross Pay
def calculate_gross_pay():
    gross_pay =  float(calculate_regular_pay() + calculate_overtime_pay()) 
    return round(gross_pay, 2)

# Calculate Federal Tax 
def calculate_fed_tax():
    fed_tax = float(calculate_gross_pay() * .015)
    return round(fed_tax, 2)

# Calculate State Tax
def calculate_state_tax():
    state_tax = float(calculate_gross_pay() * .01)
    return round(state_tax, 2)

# Calculate FICA Tax
def calculate_fica_tax():
    fica_tax = float(calculate_gross_pay() * .02)
    return round(fica_tax, 2)

# Calculate Total Tax Amount
def calculate_total_tax():
    total_tax = float(calculate_fed_tax() + calculate_state_tax() + calculate_fica_tax())
    return round(total_tax, 2)

# Calculate Net Pay
def calculate_net_pay():
    net_pay = float(calculate_gross_pay() - calculate_total_tax())
    return round(net_pay, 2)

# Display Paycheck Information 
print("\nEmployee name: " + str(employee_name))
print("Hourly rate: " + str(hourly_rate))
print("Hours worked: " + str(hours_worked))
print("Regular Pay: $", calculate_regular_pay())
print("Overtime Pay: $", calculate_overtime_pay())
print("Gross Pay: $", calculate_gross_pay())
print("Federal Tax: $", calculate_fed_tax())
print("State Tax: $", calculate_state_tax())
print("FICA Tax: $", calculate_fica_tax())
print("Total Tax: $", calculate_total_tax())
print("Net Pay: $", calculate_net_pay())