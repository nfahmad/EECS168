'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 11/24/2022
Lab: lab9
Last modified: 11/28/2022
Purpose: This file creates a class that takes data from the driver module and gives information
'''

#circle.py

from math import pi


class Circle:

    def __init__(self, radius, xPos, yPos):
        self.radius = radius
        self.xPos = xPos
        self.yPos = yPos
    
    def diameter(self):
        diameter_value = self.radius * 2

        return diameter_value
        
    def area(self):
        area_value = pi * ((self.radius)**2)
    
        return area_value
    
    def circumference(self):
        circumference_value = 2 * pi * (self.radius)

        return circumference_value
    
    def dist_to_origin(self):
        distance = (self.xPos**2 + self.yPos - 0**2)**0.5

        return distance
    
    def intersect(self, second_circle):
        sum_of_radii = self.radius + second_circle.radius

        subtraction_of_radii = self.radius - second_circle.radius

        distance_between_centers = ((second_circle.xPos - self.xPos)**2 + (second_circle.yPos - self.yPos)**2)**0.5

        if distance_between_centers < abs(subtraction_of_radii):
            intersection = False
            
        elif distance_between_centers == abs(subtraction_of_radii):
            intersection = True

        elif distance_between_centers == 0 and self.radius == second_circle.radius:
            intersection = True
        
        elif distance_between_centers <= sum_of_radii:
            intersection = True

        else:
            intersection = False

        return intersection


    