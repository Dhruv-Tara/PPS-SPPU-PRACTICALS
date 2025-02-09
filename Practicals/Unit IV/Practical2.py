# Copyright (c) 2025 Dhruv-Tara
# License : MIT

# 2. Program to access a file after it is closed 

# For this program I have created a txt file in same directory and written text in it and then closed it.

import os

file = input("Enter the file path: ")

if os.path.exists(file) :

    with open(file, 'r') as f:
        print(f.read())

else :
    print("File does not exist.")

"""
Output :
Enter the file path: C:\Users\yash\Documents\GitHub\PPS-SPPU-PRACTICALS\Practicals\Unit IV\practical2.txt
Hello World
"""