# Copyright (c) 2025 Dhruv-Tara
# License: MIT
# 1. Program to display data of different types using variable and literal constants. 

# Basic theory about variable and literal constants are that 
# Variables are used to store data values.
# Literals are data values that have fixed values.

# Variable Declaration

integer = int(input("Enter a number : "))

string = input("Enter a string : ")

floatingNumber = float(input("Enter a floating number : "))


# Displaying the data

print("first varibale is a : ",type(integer))
print("second varibale is a : ",type(string))
print("third varibale is a : ",type(floatingNumber))


"""
Output : 
Enter a number : 10
Enter a string : hello
Enter a floating number : 3.9
first varibale is a :  <class 'int'>
second varibale is a :  <class 'str'>
third varibale is a :  <class 'float'>
"""