# Copyright (c) 2025 Dhruv-Tara
# License: MIT

# 1. Program to demonstrate operation on lists 

# Creating a list of integers

lst = [1,2,3,4,5]

# Printing the list

print("The list is : ",lst)

# Printing the first element of the list

print("The first element of the list is : ",lst[0])

# Printing the last element of the list

print("The last element of the list is : ",lst[-1])

# Printing the length of the list

print("The length of the list is : ",len(lst))

# Printing the sum of the elements of the list

print("The sum of the elements of the list is : ",sum(lst))

# Printing the maximum element of the list

print("The maximum element of the list is : ",max(lst))

# Printing the minimum element of the list

print("The minimum element of the list is : ",min(lst))

# Printing the list in reverse order

print("The list in reverse order is : ",lst[::-1])

# Printing the list in sorted order

print("The list in sorted order is : ",sorted(lst))

# Adding an element to the list

lst.append(6)
print("The list after adding an element is : ",lst)

# Removing an element from the list

lst.remove(6)
print("The list after removing an element is : ",lst)

# Inserting an element at a specific index

lst.insert(2,6)
print("The list after inserting an element is : ",lst)

# Removing an element at a specific index

lst.pop(2)
print("The list after removing an element at a specific index is : ",lst)

# Extending the list with another list

lst.extend([6,7,8])
print("The list after extending with another list is : ",lst)

# Counting the number of occurences of an element in the list

print("The number of occurences of 6 in the list is : ",lst.count(6))

# Clearing the list

lst.clear()
print("The list after clearing is : ",lst)

"""
Output :
The list is :  [1, 2, 3, 4, 5]
The first element of the list is :  1
The last element of the list is :  5
The length of the list is :  5
The sum of the elements of the list is :  15
The maximum element of the list is :  5
The minimum element of the list is :  1
The list in reverse order is :  [5, 4, 3, 2, 1]
The list in sorted order is :  [1, 2, 3, 4, 5]
The list after adding an element is :  [1, 2, 3, 4, 5, 6]
The list after removing an element is :  [1, 2, 3, 4, 5]
The list after inserting an element is :  [1, 2, 6, 3, 4, 5]
The list after removing an element at a specific index is :  [1, 2, 3, 4, 5]
The list after extending with another list is :  [1, 2, 3, 4, 5, 6, 7, 8]
The number of occurences of 6 in the list is :  1
The list after clearing is :  []
"""