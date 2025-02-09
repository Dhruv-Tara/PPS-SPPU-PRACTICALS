# Copyright (c) 2025 Dhruv-Tara
# License : MIT

# 1. Program to open a file and print its attribute values. 

import os

file = input("Enter the file path: ")

if os.path.exists(file):
    print("File exists.")
    print("File size is: ", os.path.getsize(file), "bytes.")
    print("File last access time is: ", os.path.getatime(file))
    print("File last modification time is: ", os.path.getmtime(file))
    print("File creation time is: ", os.path.getctime(file))

else:
    print("File does not exist.")

""" 
Output :
Enter the file path: C://Users/yash/Downloads/setup.exe 
File exists.
File size is:  3393592 bytes.
File last access time is:  1739114071.8761094
File last modification time is:  1733644254.6351852
File creation time is:  1733644253.3587344
"""