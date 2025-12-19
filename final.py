#DND NPC generator

import random

print("Welcome to the D&D NPC generator!")
print("\nThis works specifically for Boone's sci fi game, but it can be modified to work for any game")

MimperialFirstNames = ["Sam", "Matt", "Martain", "James", "Booth", "Ben", "Killian", "Oxide", "Jeremey", "Will", "Micheal", "Kaleb", "Tim", "Skooter", "Joseph", "Simon", "Adam", "Aaron", "Isaac", "Pim", "Tony", "Steve", "Ian", "Josh", "Jake", "Snake", "Peter", "Elias", "Eli", "Angel", "Henry", "Gavin", "Devin", "Jordan", "Abraham", "Muhammod", "Tom", "Egypt"]

FimperialFirstName = ["Sam", "Alice", "Rebecca", "Witney", "Elli", "Sarah", "Aubrey", "Audrey", "Mary", "Beatrice", "Anna", "May", "Olivia", "Sydney", "Dove", "Ramona", "Beverly", "Jess", "Jenny", "Poppy", "Synthia", "Pandora", "Bloodrayn", "Rei", "Molly", "Natalie", "Slinda", "Linda", "Lucy", "Fern", "Julia", "Bell", "Diane", "Amelia", "Adda", "Abba", "Ella"]

imperialLastNames = ["Jones", "Earthan", "Euphrates", "Hamnet", "Johnson", "Stevens", "Brick", "Pinchio", "Thanker", "Localized", "Marsha", "Strovinal", "Bigidiots", "Florida", "Helsing", "Harker", "Pon", "Sweatshop", "O'Riley", "Minus", "Crusher", "Himmle", "Dreadmaw", "Catcher", "Ruth", "Gohn", "Bilth", "Barlowe", "Curve", "BigLeaper", "Rattling", "Samson", "Gleemingslick"]

alienFamilyName = ["Allack", "Uphrea", "Mothman", "Gourra", "Ipvsix", "Hand"]

alienPersonalName = ["Slaggn", "Bipol", "Igwan", "jhahass", "Limsh", "Mettir", "Ragoo"]

abominationTypes = ["Cat", "Bird", "Insect", "Tiefling", "Reptile", "All lung", "Fish", "Goblin", "Snake", "Monkey"]

def printLine():
    print("\n---------------------------------------------------------------------------")

def menue():
    printLine()
    print("\n===Main Menu===")
    print("\n1: Generate new NPC")
    print("\n2: Roll a die")
    print("\n2\3: Quit")

    choice = input("Enter choice: ").strip().lower()

    if choice == "1":
        generate()
    elif choice == "2":
        dieMenu()
    elif choice == "3":
        quit()
    else:
        print("You messed up")
        menue()

def dieMenu():
    printLine()
    print("\nType in the number of sides your dice should have")
    while True:
        sides = input("Enter sides here: ").strip().lower()

        try:
            sides = int(sides)
            if sides <= 0:
                print("dice must have more than 0 sides")
                continue
            break
        except ValueError:
            print("Please print a valid number")
    result = roll(sides)
    print(f"\nYou got: {result}")

    menue()

def roll(num):
    result = random.randint(1, num)
    return result

def generate():
    origin = pickOrigin()

    print(f"\nOrigin selected: {origin}")

    if origin == "imperial":
        gender = pickGender()
        print(f"Gender selected: {gender}")

    if origin == "imperial":
        generateImperial(gender)
        menue()
    elif origin == "alien":
        generateAlien()
        menue()
    else:
        print("You messed up")
        generate()

def pickOrigin():
    printLine()
    print("\nSelect your NPC's origin:")
    print("\n1: Imperial")
    print("\n2: Alien")
    origin = input("Enter choice here: ").strip().lower()

    if origin == "1":
        origin = "imperial"

    if origin == "2":
        origin = "alien"

    while origin != "imperial" and origin != "alien":
        origin = input("Invalid choice, chose again:").strip().lower()
        if origin == "1":
            origin = "imperial"

        if origin == "2":
             origin = "alien"

    return origin



def pickGender():
    printLine()
    print("Select gender:")
    print("\n1: Randomize")
    print("\n2: Male")
    print("\n3: Female")

    gender = input("Enter choice here: ").strip().lower()

    if gender == "1" or gender == "randomize":
        rand = random.randint(1, 2) #either 1 or 2. Pretty sure
        if rand == 1:
            gender = "male"
        else:
            gender = "female"
    
    if gender == "2":
        gender = "male"
    if gender == "3":
        gender = "female"

    while gender != "male" and gender != "female":
       
        gender = input("Invalid choice, choose again: ").strip().lower()
       
        if gender == "1" or gender == "randomize":
            rand = random.randint(1, 2) #either 1 or 2. Pretty sure
            if rand == 1:
                gender = "male"
            else:
                gender = "female"
    
        if gender == "2":
            gender = "male"
        if gender == "3":
            gender = "female"

    return gender

def generateImperial(gender):
    printLine()
    print(f"Generating a {gender} imperial citizen")
    
    firstlist = MimperialFirstNames

    if gender != "male":
        firstlist = FimperialFirstName

    firstname = random.choice(firstlist)

    lastname = random.choice(imperialLastNames)

    abomb = froskEyes()

    if abomb != "no":
        print(f"{firstname} {lastname} is a {abomb} abomination")
    else:
        print(f"{firstname} {lastname}")


def froskEyes():
    rand = random.randint(1,10)

    if rand == 1:
        isAbominant = True
    else:
        isAbominant = False

    if isAbominant:
        abomb = random.choice(abominationTypes)
    else:
        abomb = "no"

    return abomb


def generateAlien():
    printLine()
    familyName = random.choice(alienFamilyName)

    personName = random.choice(alienPersonalName)

    print(f"{familyName} {personName}")

menue()