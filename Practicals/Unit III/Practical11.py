# Copyright (c) 2025 Dhruv-Tara
# License : MIT

# 11.Write a python program that accepts a string from user and perform following string 
# operations- i. Calculate length of string ii. String reversal iii. Equality check of two strings iii. 
# Check palindrome ii. Check substring 


string = input("Enter the string: ")

print("Length of the string is: ", len(string))

print("Reversed string is: ", string[::-1])

string2 = input("Enter the second string: ")

if string == string2:
    print("Both strings are equal.")

else:
    print("Both strings are not equal.")

if string == string[::-1]:
    print("The string is a palindrome.")

else:
    print("The string is not a palindrome.")

substring = input("Enter the substring: ")

if substring in string:
    print("The substring is present in the string.")

else:
    print("The substring is not present in the string.")


"""
Output :
Enter the string: Hello World
Length of the string is:  11
Reversed string is:  dlroW olleH
Enter the second string: Hello World
Both strings are equal.
The string is not a palindrome.
Enter the substring: World
The substring is present in the string.
"""
