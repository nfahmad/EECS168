'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 9/12/2022
Lab: lab02
Last modified: 9/12/2022
Purpose: Obtain a wind speed from the user and tell them either what category or type of storm.
'''

wind_speed = int(input("Input a wind speed (m/s): "))

if wind_speed >= 70:
	print("A wind speed of" , wind_speed , "m/s is a Category 5 hurricane.")
elif 58 <= wind_speed <= 69:
	print("A wind speed of" , wind_speed , "m/s is a Category 4 hurricane.")
elif 50 <= wind_speed <= 57:
	print("A wind speed of" , wind_speed , "m/s is a Category 3 hurricane.")
elif 43 <= wind_speed <= 49:
	print("A wind speed of" , wind_speed , "m/s is a Category 2 hurricane.")
elif 33 <= wind_speed <= 42:
	print("A wind speed of" , wind_speed , "m/s is a Category 1 hurricane.")
elif 18 <= wind_speed  <= 32:
	print("A wind speed of" , wind_speed , "m/s is a tropical storm.")
elif 0 <= wind_speed <= 17:
	print("A wind speed of" , wind_speed , "m/s is a tropical depression.")
else:
	print("Invalid wind speed")

