# Copyright (c) 2025 Dhruv-Tara
# License: MIT

# 6. Program to calculate the sum and average of first 10 numbers 

# Taking the first 10 numbers

sum = 0

for i in range(0,11) : # Since the range function is exclusive of the last number, we have to take 11 to include 10
    sum = sum + i

average = sum/10

print("The sum of first 10 numbers is : ", sum)

print("The average of first 10 numbers is : ", average)

"""
Output:
The sum of first 10 numbers is :  55
The average of first 10 numbers is :  5.5
"""
