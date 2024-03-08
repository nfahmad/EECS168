'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 12/07/22
Lab: lab08
Last modified: 12/08/22
Purpose: Load records of certain drivers license information
'''

#dmv.py

from driverslicense import DriversLicense

class DMV:
    def __init__(self, _filename):
        self.drivers = []

        self.order = []

        self._filename = _filename

        _filename = open(_filename, "r")

        for line in _filename:
                line = line.strip().split()
                driver = DriversLicense(int(line[0]), line[1], line[2], int(line[3]), line[4])
                self.order.append(driver.license_number())
                self.drivers.append(driver)

        self.order = sorted(self.order, reverse = True)
    
    def print_menu(self):
        print(" ")
        print("Select an option:")
        print("1) Print all Drivers Info, sorted by drivers license numbers")
        print("2) Print all young, unregistered voters")
        print("3) Print drivers by last initial")
        print("4) Print drivers of a specific age")
        print("5) Quit")

    def run(self):
        while True:
            self.print_menu()

            self.user_input = int(input("Enter your choice: "))
            print(" ")

            if self.user_input == 1:
                for num in self.order:
                    for item in self.drivers:
                        if item.license_number() == num:
                            print(item)
            
            elif self.user_input == 2:
                for num in self.order:
                    for item in self.drivers:
                        if item.license_number() == num and item.age() in range (18, 25) and item.voter_status() == "N":
                            print(item)

            elif self.user_input == 3:
                initial = input("Enter a letter initial to sort by: ")
                print(" ")
                initial = initial.upper()
                
                list(initial)
                list_of_initials = []

                for item in self.drivers:
                    if item.last_name()[0] == initial[0]:
                        list_of_initials.append(item.last_name()[0])
                if initial in list_of_initials:
                    for num in self.order:
                        for item in self.drivers:
                            if item.license_number() == num and item.last_name()[0] == initial[0]:
                                print(item)
                else:
                    print("No record found.")
            
            elif self.user_input == 4:
                ages = []

                select = int(input("Enter an age to sort by: "))
                print(" ")
                for item in self.drivers:
                    if item.age() == select:
                        ages.append(item.age())

                if select in ages:
                    for num in self.order:
                        for item in self.drivers:
                            if item.license_number() == num and item.age() == select:
                                print(item)
                
                else:
                    print("No record found.")
            
            elif self.user_input == 5:
                break

            else:
                print("This is an invalid input")



    

    