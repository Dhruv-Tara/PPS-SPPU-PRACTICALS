# Copyright (c) 2025 Dhruv-Tara
# License : MIT

# 7. Program to understand ord() and char() function.

# ord() function is used to get the ASCII value of a character.
# char() function is used to get the character from an ASCII value.

char = input("Enter the character: ")

print("ASCII value of the character is: ", ord(char))

ascii_val = int(input("Enter the ASCII value: "))

print("Character of the ASCII value is: ", chr(ascii_val))

""" 
Output :
Enter the character: A
ASCII value of the character is:  65
Enter the ASCII value: 68
Character of the ASCII value is:  D
"""
