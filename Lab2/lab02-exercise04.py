'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 9/16/2022
Lab: lab02
Last modified: 9/16/2022
Purpose: Create a program that takes a number of sodas and then tells the user how many Fridge Cubes, six packs, and single sodas it will be packaged as
'''


sodas = int(input("How many sodas do you have? "))

fridge_cubes = sodas//24

soda_remainder = sodas%24

six_packs = soda_remainder//6

six_packs_remainder = soda_remainder%6

print("Fridge Cubes:" , fridge_cubes)
print("Six-packs:" , six_packs)
print("Singles:" , six_packs_remainder)

