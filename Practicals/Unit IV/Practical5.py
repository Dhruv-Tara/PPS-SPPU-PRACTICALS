# Copyright (c) 2025 Dhruv-Tara
# License : MIT

# 5. Program to display the contents of a file. 

import os

file = input("Enter the file path: ")

if os.path.exists(file) :
    
    with open(file,'r') as f:
        print(f.read())
        pass
    pass

else :
    print("File does not exist.")
    pass


"""
Output :
Enter the file path: C:\Users\yash\Documents\GitHub\PPS-SPPU-PRACTICALS\Practicals\Unit IV\practical5.txt
Practical 5 test file
"""
