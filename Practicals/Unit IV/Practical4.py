# Copyright (c) 2025 Dhruv-Tara
# License : MIT

# 4. Program to append data to an already existing file. 

import os

file = input("Enter the file path: ")

if os.path.exists(file) :

    file_text = input("Enter the text to append in the file: ")

    with open(file,'a') as f:
        f.write(file_text)
        pass
    pass

else :
    print("File does not exist.")
    pass


"""
Output :
Enter the file path: C:\Users\yash\Documents\GitHub\PPS-SPPU-PRACTICALS\Practicals\Unit IV\practical4.txt
Enter the text to append in the file: This is the appended text 
"""