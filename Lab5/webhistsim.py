'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 10/07/22
Lab: lab05
Last modified: 10/20/2022
Purpose: Write a program that simulates creating a web browser history
'''

history = []

position = 0

while True:
	command = input("Enter a command: ")
	command_split = command.split()

	if command_split[0] == "NAVIGATE":
		history = history[0: position]
		history.append(command_split[1])
		position += 1

	elif command_split[0] == "BACK":
		if position < len(history)-1:
			position = len(history)
			print("Can't go back")
			print(" ")
		else:
			position -= 1

	elif command_split[0] == "FORWARD":
		if position > len(history)-1:
			position = len(history)
			print("Can't go forward")
			print(" ")
		else:
			position += 1

	elif command_split[0]== "HISTORY":
		print(" ")
		print("Oldest")
		print("===========")
		for num in range(len(history)):
			if num == position - 1:
				print(f"{history[num]} <==")
			else:
				print(history[num])
		print("===========")
		print("Newest")
		print(" ")

	elif command_split[0] == "EXIT":
		break

	else:
		print("Invalid input")
		print(" ")

