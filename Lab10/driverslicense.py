'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 12/07/22
Lab: lab08
Last modified: 12/08/22
Purpose: Overload multiple operators/methods
'''

#driverslicense.py

class DriversLicense:
    
    def __init__(self, license_number, first_name, last_name, age, voter_status):
        self._license_number = int(license_number)
        self._first_name = first_name
        self._last_name = last_name
        self._age = int(age)
        self._voter_status = voter_status

        if self._voter_status == "Y":
            self._registered = "registered"
        else:
            self._registered = "not registered"
    
    def license_number(self):
        return self._license_number
    
    def last_name(self):
        return self._last_name
    
    def age(self):
        return self._age

    def voter_status(self):
        return self._voter_status

    def __lt__(self, other):
        if self._license_number < other._license_number:
            return True

        else:
            return False
    
    def __gt__(self, other):
        if self._license_number > other._license_number:
            return True

        else:
            return False

    def __le__(self, other):
        if self._license_number <= other._license_number:
            return True

        else:
            return False

    def __ge__(self, other):
        if self._license_number >= other._license_number:
            return True

        else:
            return False

    def __eq__(self, other):
        if self._license_number == other._license_number:
            return True

        else:
            return False

    def __ne__(self, other):
        if self._license_number != other._license_number:
            return True

        else:
            return False

    def __str__(self):
        output = (f"{self._last_name}, {self._first_name} ({self._age}): {self._license_number} {self._registered}")

        return output

    def __repr__(self):
        output = f"{self._last_name}, {self._first_name} ({self._age}): {self._license_number} {self._registered}"

        return output

    