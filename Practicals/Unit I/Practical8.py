# Copyright (c) 2025 Dhruv-Tara
# License: MIT

"""
8. To calculate salary of an employee given his basic pay (take as input from user). Calculate gross 
salary of employee. Let HRA be 10 % of basic pay and TA be 5% of basic pay. Let employee pay 
professional tax as 2% of total salary. Calculate net salary payable after deductions.
"""

# Taking basic pay as input from user

basicPay = float(input("Enter the basic pay of the employee : "))

# Calculating HRA

HRA = 0.1 * basicPay
TA = 0.05 * basicPay
TotalSalary = basicPay + HRA + TA
professtionalTax = 0.02 * TotalSalary
netSalary = TotalSalary - professtionalTax

# Printing the result

print("The gross salary of the employee is : ",netSalary)


"""
Output :
Enter the basic pay of the employee : 50000
The gross salary of the employee is :  56350.0
"""