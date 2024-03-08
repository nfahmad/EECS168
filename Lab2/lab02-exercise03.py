'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 9/20/2022
Lab: lab02
Last modified: 9/20/2022
Purpose: Ask the user what restaurant items they would like and print a reciept with tax
'''


cold_pasta_price = float(2.50)
grilled_cheese_price = float(5.55)
pie_price = float(3.00)


print("=========================")
print("WELCOME TO THE RESTAURANT")
print("=========================")

cold_pasta = input("Do you want Cold Pasta? (y/n): ")
if cold_pasta.lower() == "y":
	cold_pasta_amount = int(input("How many?: "))
else: cold_pasta_amount = 0
if cold_pasta_amount < 0:
	cold_pasta_amount = 0
cold_pasta_total = float(cold_pasta_amount*cold_pasta_price)


grilled_cheese = input("Do you want Grilled Cheese? (y/n): ")
if grilled_cheese.lower() == "y":
	grilled_cheese_amount = int(input("How many?: "))
else: grilled_cheese_amount = 0
if grilled_cheese_amount < 0:
	grilled_cheese_amount = 0
grilled_cheese_total = float(grilled_cheese_amount*grilled_cheese_price)


pie = input ("Do you want Pie? (y/n): ")
if pie.lower() == "y":
	pie_amount = int(input("How many?: "))
else: pie_amount = 0
if pie_amount < 0:
	pie_amount = 0
pie_total = float(pie_amount*pie_price)

subtotal = (1.08*(cold_pasta_total+grilled_cheese_total+pie_total))
tax = subtotal-(cold_pasta_total+grilled_cheese_total+pie_total)

user_age = int(input("How old are you?: "))
if(user_age <= 5):
	pie_total = 0
	subtotal = (1.08*(cold_pasta_total+grilled_cheese_total+pie_total))
	tax = subtotal-(cold_pasta_total+grilled_cheese_total+pie_total)
	discount = 0
elif(user_age >= 55):
	discount = 0.55*subtotal
else: discount = 0

total = subtotal-discount


print(f"{cold_pasta_amount} Cold Pasta @ {cold_pasta_price:0.2f} ==> {cold_pasta_total:0.2f}")
print(f"{grilled_cheese_amount} Grilled Cheese @ {grilled_cheese_price:0.2f} ==> {grilled_cheese_total:0.2f}")
print(f"{pie_amount} Pie @ {pie_price:0.2f} ==> {pie_total:0.2f}")
print(f"Subtotal: ${subtotal:0.2f}")
print(f"Tax: ${tax:0.2f}")
print(f"Discount: ${discount:0.2f}")
print("=========================")
print(f"Total: ${total:0.2f}")
print("Please come again!")



