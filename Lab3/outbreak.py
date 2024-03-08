'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 09/28/2022
Lab: lab03
Last modified: 09/28/2022
Purpose: Make a program that will ask the user for what day they want a count of people with the flu for. Then display the amount
'''

print("OUTBREAK!")

user_day = int(input("What day do you want a sick count for?: "))

day_one = 1

day_two = 4

day_three = 64

day_total = day_one+day_two+day_three

if user_day <= 0:
	print("Invalid day")
elif  user_day == 1:
	print("Total people with flu: 1")
elif user_day == 2:
	print("Total people with flu: 4")
elif user_day == 3:
	print("Total people with flu: 64")
else:
	for i in range (user_day-4):
		day_one = day_two
		day_two = day_three
		day_three = day_total
		day_total = day_one+day_two+day_three
	print(f"Total people with flu: {day_total}")

