
"""#################Task : Ask the user for their name and print a greeting IN UPPERCASE.###########
- input() to read a name
- .strip() to remove extra spaces
- .upper() to convert to uppercase
- '+' to *concatenate* (join) strings together
- print() to display the final message.
 We also show an f-string alternative for comparison.
"""

name = input("Please type your name: ").strip()  
greeting_with_plus = "HELLO, " + name.upper() + "! WELCOME "
greeting_with_fstring = f"Hello, {name.upper()}!" 
print(greeting_with_plus)        
print(greeting_with_fstring)     


#----------------------------easy-------------------------------#
"""1. Write a Python script to parse a CSV file."""
import csv

# Open the CSV file
with open( r'C:\Users\namra\Downloads\de_assignment_namratha (1)\easy\data\sample.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)  # Reads rows as dictionaries
    for row in reader:
        print(row)

        #-----------------------------easy 2-----------------------#