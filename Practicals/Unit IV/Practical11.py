# Copyright (c) 2025 Dhruv-Tara
# License : MIT

# 11. Program that counts the number of tabs, space and newline character in a file. 11. Program that counts the number of tabs, space and newline character in a file. 
# Using the file practical8.txt created in Practical 8

file_path = input("Enter the path of the file: ")

with open(file_path, "r") as file:
    data = file.read()


tabs = data.count("\t")
spaces = data.count(" ")
newlines = data.count("\n")

print("Number of tabs in the file:", tabs)
print("Number of spaces in the file:", spaces)
print("Number of newlines in the file:", newlines)

""" 
Output :
Enter the path of the file: C:\Users\yash\Documents\GitHub\PPS-SPPU-PRACTICALS\Practicals\Unit IV\practical8.txt
Number of tabs in the file: 0
Number of spaces in the file: 170
Number of newlines in the file: 6
"""