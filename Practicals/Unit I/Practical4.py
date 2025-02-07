# Copyright (c) 2025 Dhruv-Tara
# License: MIT

# 4. Program to perform all operation (addition, multiplication, subtraction, division, modules) and expression. 

# Taking two numbers to perform operations

firstNumber = int(input("Enter the first number : "))
secondNumber = int(input("Enter the second number : "))

# Performing addition operation

addition = firstNumber + secondNumber

# Performing multiplication operation

multiplication = firstNumber * secondNumber

# Performing subtraction operation

subtraction = firstNumber - secondNumber

# Performing division operation

division = firstNumber / secondNumber

# Performing modules operation

modules = firstNumber % secondNumber

# Performing expression

expression = (firstNumber + secondNumber) * (firstNumber - secondNumber)

# Printing the results

print("The addition of the two numbers is : ",addition)
print("The multiplication of the two numbers is : ",multiplication)
print("The subtraction of the two numbers is : ",subtraction)
print("The division of the two numbers is : ",division)
print("The modules of the two numbers is : ",modules)
print("The expression of the two numbers is : ",expression)

"""
Output :
Enter the first number : 10
Enter the second number : 5
The addition of the two numbers is :  15
The multiplication of the two numbers is :  50
The subtraction of the two numbers is :  5
The division of the two numbers is :  2.0
The modules of the two numbers is :  0
The expression of the two numbers is :  75
"""
