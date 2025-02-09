# Copyright (c) 2025 Dhruv-Tara
# License : MIT

# 3. Program to write a file using the writelines() method. 

import os 

file = input("Enter the file path: ")

if os.path.exists(file) :

    file_text = input("Enter the text to write in the file: ")

    with open(file,'w') as f:
        f.writelines(file_text)
        pass
    pass

else :
    print("File does not exist.")
    pass

"""
Output :
Enter the file path: C:\Users\yash\Documents\GitHub\PPS-SPPU-PRACTICALS\Practicals\Unit IV\practical3.txt
Enter the text to write in the file: Hello How are you Today
"""