# Copyright (c) 2025 Dhruv-Tara
# License : MIT

# 8. Program that reads data from a file and calculates the percentage of vowels and consonants in the file. 
# Made a file with essay named "The Importance of Reading"

import os

file = input("Enter the file path: ")

if os.path.exists(file) :

    vowels = ['a','e','i','o','u']

    listOfWords = []

    NoOfVowels = 0
    NoOfConsonants = 0

    with open(file,'r') as f:
        data = f.read()
        listOfWords = data.split(" "or"\n")
        pass
    
    for word in listOfWords :
        word = word.lower()
        
        for letter in word :
            if letter in vowels :
                NoOfVowels += 1
                pass
            else :
                NoOfConsonants += 1
                pass
            pass

        pass

    total = NoOfVowels + NoOfConsonants

    print("Percentage of Vowels: ",(NoOfVowels/total)*100)
    print("Percentage of Consonants: ",(NoOfConsonants/total)*100)
    pass

else :

    print("File does not exist.")
    pass

""" 
Output :
Enter the file path: C:\Users\yash\Documents\GitHub\PPS-SPPU-PRACTICALS\Practicals\Unit IV\practical8.txt
Percentage of Vowels:  37.93103448275862
Percentage of Consonants:  62.06896551724138
"""