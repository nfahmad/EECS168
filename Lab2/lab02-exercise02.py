'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 9/12/2022
Lab: lab02
Last modified: 9/12/2022
Purpose: Obtain a numerator and denominator from the user. Then, display resulting long division.
'''

numerator = int(input("Enter a numerator: "))

denominator = int(input("Enter a denominator: "))


if denominator == 0:
	print("Sorry, you may not divide by zero.")
else:
	print(numerator , "/" , denominator , "=" , numerator//denominator , "Remainder" , numerator%denominator)
print("Exiting...")

