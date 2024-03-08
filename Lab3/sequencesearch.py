'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 09/23/2022
Lab: lab03
Last modified: 09/23/2022
Purpose: Obtain a string from the user, ask the user if they want a case-sensitive search, ask the user for a sequence of characters in the string, and print the count of occurences of the user entered sequence into the string
'''

user_string = input("Enter a string: ")

case_sensitive = input("Do you want a case-sensitive match? (y/n): ")

sequence = input("Enter a seqence to count: ")


if case_sensitive.lower() == "y":
	sequence_count = user_string.count(sequence)
else: sequence_count = user_string.lower().count(sequence.lower())

print("In the string" , user_string , "the sequence" , sequence , "occurs" , sequence_count , "time(s)")
