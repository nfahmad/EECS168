'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 12/07/22
Lab: lab08
Last modified: 12/08/22
Purpose: Make sure the file name was passed in, then hand control over to the DMV class
'''

#main.py

from dmv import DMV

def main():
    user_input = input("Please enter the file name: ")

    myDMV = DMV(user_input)
    myDMV.run()

if __name__ == "__main__":
    main()

