'''
Author: Nabeel Ahmad
KUID: 3096518
Date: 11/14/22
Lab: lab08
Last modified: 11/15/22
Purpose: Load a pokedex and have the user interact with it in various ways. Create random teams, have pokemon fight, and look up translations
'''

import random

def build_pokedex(filename):
    pokedex = {}

    for line in filename:
        names = line.split()

        pokedex[names[0]] = names[1]

    return pokedex

def build_team(pokedex, size=6, is_unique=False):
    pokemon = list(pokedex.keys())

    if is_unique == True:
        team = random.sample(pokemon, k=size)

    else:
        team = random.choices(pokemon, k=size)
    
    return team

def battle(team1, team2):
    print('+++Team 1+++')

    for x in range(len(team1)):
        print(team1[x])
    
    print(" ")

    print('+++Team 2+++')

    for x in range(len(team2)):
        print(team2[x])

    print(" ")

    round_number = 1

    while len(team1) >0 and len(team2) >0:
        print(f"+++Round {round_number}+++")

        team1_pokemon = team1[0]
        team2_pokemon = team2[0]

        print((f"{team1_pokemon} VS {team2_pokemon}"))

        possible_winner = [team1_pokemon, team2_pokemon]

        round_winner = random.choice(possible_winner)

        print(f"{round_winner} wins!")

        print(" ")

        if round_winner == team1_pokemon:
            team2.pop(0)

        elif round_winner == team2_pokemon:
            team1.pop(0)

        round_number += 1

    if len(team1) > 0:
        print('+++Team 1 Wins!+++')

        for x in range(len(team1)):
            print(team1[x])

    if len(team2) > 0:
        print('+++Team 2 Wins!+++')

        for x in range(len(team2)):
            print(team2[x])


def print_menu():
    print(" ")
    print("1) Print Pokedex")
    print("2) Translate")
    print("3) Build a team")
    print("4) Pokemon battle")
    print("5) Exit")

def main():
    file = open("pokedex.txt", "r")
    
    pokedex = build_pokedex(file)

    while True:
        print_menu()

        user_input = int(input("Please enter a number: "))

        print(" ")

        if user_input == 1:
            for key, value in pokedex.items():
                print(f"{key} : {value}")

        elif user_input == 2:
            us_name = input("What US name do you want translated to the JPN equivalent?: ")

            if us_name in pokedex.keys():
                print(pokedex[us_name])

            else:
                print("This US pokemon name is not in the pokedex, please try again.")

        elif user_input == 3:
            a_team = build_team(pokedex)

            for x in range(len(a_team)):
                print(a_team[x])

        elif user_input == 4:
            team1 = build_team(pokedex)
            team2 = build_team(pokedex)

            battle(team1, team2)

        elif user_input == 5:
            break 

        else:
            print("This is an invalid input, please try again")

main()
