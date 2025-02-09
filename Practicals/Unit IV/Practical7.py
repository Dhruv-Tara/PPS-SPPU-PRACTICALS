# Copyright (c) 2025 Dhruv-Tara
# License : MIT

# 7. Program that tells and sets the position of the file pointer. 
# Using Practical 5 file.

import os

file = input("Enter the file path: ")

if os.path.exists(file) :
    
    with open(file,'r') as f:
        print("Current position of file pointer: ",f.tell())
        f.seek(0)
        print("Position of file pointer after setting it to 0: ",f.tell())
        pass
    pass

else :
    
    print("File does not exist.")
    pass

# """ 
# Output :
# Enter the file path: C:\Users\yash\Documents\GitHub\PPS-SPPU-PRACTICALS\Practicals\Unit IV\practical5.txt
# Current position of file pointer:  0
# Position of file pointer after setting it to 0:  0
# """