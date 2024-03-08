'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 09/30/22
Lab: lab04
Last modified: 10/05/22
Purpose: Write a program to help the user make a grocery list, check off things they've grabbed, as well as get some practice making a text-based menu.
'''

shopping_list = []


while True:
	print("Welcome to your Shopping List!")
	print("1) Add item")
	print("2) Check off item")
	print("3) Print list")
	print("4) Exit")
	
	user_choice = int(input("Enter a choice: "))
	if user_choice == 1:
		add = input("What will you add to the list: ")
		shopping_list.append(add)
		print(" ")
	elif user_choice == 2:
		item = int(input("Which item will you check off?: "))-1
		item_store = shopping_list[item]
		item_check = item_store[0]
		last_letter = item_store[-1]
		for i in range(len(item_store) -1):
			if(i != 0 and i != len(item_store)):
				cross = "-"
				item_check += cross
		item_check += last_letter
		shopping_list[item] = item_check
		print(" ")
	elif user_choice == 3:
		count=1
		for line in shopping_list:
			print(f"{count}) {line}")
			count+=1
		print(" ")
	elif user_choice == 4:
		print("Goodbye!")
		break
	else:
		print("Invalid choice")
		print(" ")
