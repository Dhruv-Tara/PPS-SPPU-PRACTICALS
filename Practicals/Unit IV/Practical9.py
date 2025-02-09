# Copyright (c) 2025 Dhruv-Tara
# License : MIT

# 9. Program that changes the current directory to our newly created directory.

import os

new_directory = "NewDirectory"

if not os.path.exists(new_directory):
    os.mkdir(new_directory)
    print(f"Directory '{new_directory}' created successfully.")
else:
    print(f"Directory '{new_directory}' already exists.")


os.chdir(new_directory)
print("Current directory changed to:", os.getcwd())


""" 
Output :
Directory 'NewDirectory' created successfully.
Current directory changed to: C:\Users\yash\Documents\GitHub\PPS-SPPU-PRACTICALS\Practicals\Unit IV\NewDirectory
"""
