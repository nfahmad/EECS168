'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 09/28/2022
Lab: lab03
Last modified: 09/28/2022
Purpose: Create a program that will make the user guess the secret phrase "bringcoffee". The game won't end until the user guesses phrase, but along the way you will help the user
'''

phrase = "bringcoffee"

guess_amount = 0

while True:
	user_guess = input("Guess: ")
	guess_amount += 1
	if len(user_guess) < len(phrase):
		print("Too few characters")
	elif len(user_guess) > len(phrase):
		print("Too many characters")
	else:
		if user_guess.lower() == phrase:
			print("Correct")
			break
		else:
			count = 0
			x = 0
			for letter in user_guess.lower():
				if letter == phrase[x]:
					count += 1
				x += 1
			print(f"Correct letters: {count}")

print(f"Number of guesses: {guess_amount}")
