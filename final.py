#DND NPC generator

import random

print("Welcome to the D&D NPC generator!")
print("\nThis works specifically for Boone's sci fi game, but it can be modified to work for any game")

imperialFirstNames = []

imperialLastNames = []

alienFamilyName = []

alienPersonalName = []

abominationTypes = []

def printLine():
    print("\n---------------------------------------------------------------------------")

def menue():
    printLine()
    print("\n===Main Menu===")
    print("\n1: Generate new NPC")
    print("\n2: Quit")

def generate():
    print("\nSelect your NPC's origin:")
    print("\n1: Imperial")
    print("\n2: Alien")
    origin = input("Enter choice here: ").strip().lower()

    if origin == "1":
        origin = "imperial"

    if origin == "2":
        origin = "alien"

    while origin != "imperial" or origin != "alien":
        origin = input("Invalid choice, chose again:").strip().lower()
        if origin == "1":
            origin = "imperial"

        if origin == "2":
             origin = "alien"

    print(f"\nOrigin selected: {origin}")
    print("Select gender:")
    print("\n1: Randomize")
    print("\n2: Male")
    print("\n3: Female")

    gender = input("Enter choice here: ").strip().lower()

    if gender == "1" or gender == "randomize":
        rand = random.randint(1, 3) #either 1 or 2. Pretty sure
        if rand == 1:
            gender = "male"
        else:
            gender = "female"
    
    if gender == "2":
        gender = "male"
    if gender == "3":
        gender = "female"

    while gender != "male" or gender != "female":
       
        gender = input("Invalid choice, choose again: ").strip().lower()
       
        if gender == "1" or gender == "randomize":
            rand = random.randint(1, 3) #either 1 or 2. Pretty sure
            if rand == 1:
                gender = "male"
            else:
                gender = "female"
    
        if gender == "2":
            gender = "male"
        if gender == "3":
            gender = "female"