# Copyright (c) 2025 Dhruv-Tara
# License : MIT

# 10. Program to print the absolute path of a file using os.path.join 

import os


directory = "Unit IV"
filename = "practical8.txt"

file_path = os.path.join(directory, filename)

absolute_path = os.path.abspath(file_path)

print("Absolute path of the file:", absolute_path)

""" 
Output :
Absolute path of the file: C:\Users\yash\Documents\GitHub\PPS-SPPU-PRACTICALS\Practicals\Unit IV\Unit IV\practical8.txt
"""