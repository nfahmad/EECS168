'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 10/21/22 
Lab: lab06
Last modified: 10/27/22
Purpose: Perform several functions and definitions
'''

def last_digit(num):
    " " "Returns the last digit in the number" " "
    return num % 10

def remove_last_digit(num):
    " " "Returns the number with the last digit trimmed off" " "
    removed = (num - last_digit(num)) / 10
    return removed

def add_digit(current_num, new_digit):
    " " "Returns the current number with a new digit placed into the ones space" " "
    return (new_digit) + (current_num * 10)

def reverse(num):
    " " "Returns the reverse of the number" " "
    reversed_number = 0

    while num != 0:
        digit = last_digit(num)
        reversed_number = reversed_number * 10 + digit
        num //= 10

    return reversed_number

def is_palindrome(num):
    " " "Returns true if the number is a palindrome and false if the number is not a palindrome" " "
    if num == reverse(num):
        return True
    else:
        return False

def count_digits(num):
    " " "Returns the number of digits in the number" " "
    count = len(str(num))
    return count

def sum_digits(num):
    " " "Returns the sum of digits in the number" " "
    total = 0

    while num != 0:
        total += last_digit(num)
        num = remove_last_digit(num)
    
    return int(total)

def print_menu():
    " " "Prints the menu" " "
    print("1) Count digits")
    print("2) Sum digits")
    print("3) Is Palindrome")
    print("4) Reverse")
    print("5) Exit")

def main():
    " " "Until the user wants to quit, this main will print the menu, obtain the user's choice, and call the appropriate functions to print the desired results" " "
    while True:
        print_menu()
        user_choice = int(input("Choice: "))
        print(" ")

        if user_choice == 1:
            num = int(input("Please enter a positive integer: "))
            print(count_digits(num))
            print(" ")

        elif user_choice == 2:
            num = int(input("Please enter a positive integer: "))
            print(sum_digits(num))
            print(" ")

        elif user_choice == 3:
            num = int(input("Please enter a positive integer: "))
            print(is_palindrome(num))
            print(" ")

        elif user_choice == 4:
            num = int(input("Please enter a positive integer: "))
            print(reverse(num))
            print(" ")
        
        elif user_choice == 5:
            break

main()


        




