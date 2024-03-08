'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 11/24/2022
Lab: lab9
Last modified: 11/28/2022
Purpose: This file takes data from a class and gives information
'''

#main.py

from circle import Circle


def user_circle():
    
    print("Enter information for Circle:")

    radius = float(input("Radius: "))

    xPos = float(input("X Position: "))

    yPos = float(input("Y Position: "))

    print(" ")

    return Circle(radius, xPos, yPos)
    

def print_circle_info(circ, name="Circle"):

    print(" ")

    print(f"Information for {name}:")

    print(f"location: ({circ.xPos}, {circ.yPos})")

    print(f"diameter: {circ.diameter()}")

    print(f"area: {circ.area()}")

    print(f"circumference: {circ.circumference()}")

    print(f"distance from the origin: {int(circ.dist_to_origin())}")

    print(" ")

    return 0


def main():
    circle1 = user_circle()
    circle2 = user_circle()

    print_circle_info(circle1, "Circle One")
    print_circle_info(circle2, "Circle Two")

    if circle1.intersect(circle2):
        print("The circles intersect")
    else:
        print("The circles do not intersect")

    return 0

main()


