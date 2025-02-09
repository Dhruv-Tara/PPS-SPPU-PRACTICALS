# Copyright (c) 2025 Dhruv-Tara
# License : MIT

# 6. Program to split the line into a series of words and use space to perform the split operation. 
# Using Practical 5 file.

import os

file = input("Enter the file path: ")

if os.path.exists(file) :
    
    with open(file,'r') as f:
        for line in f:
            print(line.split())
            pass
        pass
    pass

else :

    print("File does not exist.")
    pass


# """
# Output :
# Enter the file path: C:\Users\yash\Documents\GitHub\PPS-SPPU-PRACTICALS\Practicals\Unit IV\practical5.txt
# ['Practical', '5', 'test', 'file']
# """