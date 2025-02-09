# Copyright (c) 2025 Dhruv-Tara
# License : MIT

# 10. Program to reverse of string by user defined function. 


def reverseString(string) -> str:
    """It Reverses The given string

    Args:
        string (str): The string to be reversed

    Returns:
        str: The reversed string
    """

    return string[::-1]


string = input("Enter the string: ")

print("The reversed string is: ", reverseString(string))

"""
Output :
Enter the string: This is a python program
The reversed string is:  margorp nohtyp a si sihT
"""