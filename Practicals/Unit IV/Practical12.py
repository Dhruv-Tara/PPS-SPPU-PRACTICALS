# Copyright (c) 2025 Dhruv-Tara
# License : MIT

# 12. To copy contents of one file to another. While copying a) all full stops are to be replaced with 
# commas b) lower case are to be replaced with upper case c) upper case are to be replaced with 
# lower case. 
# Using the file practical8.txt created in Practical 8

file_path = input("Enter the path of the file: ")
new_file_path = input("Enter the path of the new file: ")

with open(file_path, "r") as file:
    data = file.read()

data = data.replace(".", ",")
data = data.swapcase()

with open(new_file_path, "w") as file:
    file.write(data)

print("File copied successfully! with changes")


""" 
Output :
Enter the path of the file: C:\Users\yash\Documents\GitHub\PPS-SPPU-PRACTICALS\Practicals\Unit IV\practical8.txt
Enter the path of the new file: C:\Users\yash\Documents\GitHub\PPS-SPPU-PRACTICALS\Practicals\Unit IV\practical12.txt
File copied successfully! with changes
"""