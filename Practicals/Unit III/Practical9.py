# Copyright (c) 2025 Dhruv-Tara
# License : MIT

# 9. Program that counts the occurrences of a character in a string. Do not use built in function. 

string = input("Enter the string: ")
char = input("Enter the character: ")

count = 0

for i in string:
    if i == char:
        count += 1
        continue
    continue

print("The character", char, "occurs", count, "times in the string", string)

"""
Output :
Enter the string: Hello World
Enter the character: l
The character l occurs 3 times in the string Hello World
"""
