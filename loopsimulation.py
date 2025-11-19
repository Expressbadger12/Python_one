#loop simulation.py
#

#function to make visual divider line

def print_divider():
    
    print("\n" + "-" * 50 + "\n")

#this function asks the player for their name and returns it

def get_player_name():
    #ask the user to type their name
    name = input("Welcome explorer, what's your name? ")
    return  name

# this function displays options and returns a valid choice
def get_player_choice(options):
    # use while loop to keep asking until the user enters a valid choice
    while True:
        #print each option using a for loop
        for key, description in options.items():
            print(f"{key}, {description}")

        choice = input("Please enter the number of your choice: ")

        if choice in options:
            return choice
        else:
            print("\n that is not a valid choice. Please try again. \n")

def show_intro():
    #call print_divider
    print_divider()

    print("Welcome to the Loop Quest simulation")
    print("In this adventure, your decisions are powered by loops and functions")
    print("you will explore a magical world as we secretly practice Python concepts")

    name = get_player_name

    print(f"\n Nice to meet you, {name}! Let's begin your journey ")

    return name

# This function represents the forest path in teh story
#It takes name as a parameter so we can personalize the messages
#It returns a score based on what the player does
def forest_path(name):
    print_divider()

    print(f" {name}, you chose to enter the Enchanted forest")
    print("The forest is quiet and you feel a soft glow around you")

    score = 0

    forest_tasks = {
        "Cross a arrow bridge over a rive"
        "Solve a glowing rune puzzle on a stone"
        "Help a lost traveler find their way"
    }

    for task in forest_tasks:
        # describe the current task
        print(f"\n you encounter a challenge: {task}")

        answer = input("do you want to attempt this challenge? (y/n)").lower().strip()

        if answer == "y":
            print("You bravely complete teh challenge and get 10 points.")
            score += 10

        elif answer == "n":
            print("You decide to skip this challenge and move on")

        else:
            print("You do nothing.")

    print(f"\nYou leave the forest with a score of {score} points")

    return score

#This functin represents the city path in the story
def city_path(name):
    print_divider()

    print(f"{name}, you chose to explore the cyber city")
    print("Neon lights flash around you and the air buzzes with energy")

    score = 0

    visits = 0

    while visits  < 3:
        print(f"\n you have visisted {visits} district(s) so far")

        options = {
            "1": "Tech Market ( trade gadgets for knowledge points)",
            "2": "Energy plaza (restore your stamina with glowing drinks)",
            "3": "Sky rails (take a quick tour of the skyline and end your city visit)",
        }

        #Call get_player_cho
        district_choice = get_player_choice(options)

        if district_choice == "1":
            print("\nYou explore the tech market and trade with the venders")

            score += 8
            visits += 1
        elif district_choice == "2":
            print("\n You relax at the energy plaza and feel refreshed")
            score += 5
            visits += 1
        elif district_choice == "3":
            print("\nYou ride the sky rail and enjoy the beautiful city view")
            print("\n your city adventure ends")
            score += 12
            visits += 1

            break
        # this else block will not normally run because get_player_choice guarantees a valid choice
        # it is an include for completeocity
        else:
            print("\n Something unexpected happened in the city")
            continue
    #after the loop ends we print a summery message
    print(f"\nYou leave the city with a score of {score} points.")
    return score

#This function asks the player which main path they want to take
def choose_main_path(name):
    print_divider()

    print("\n You stand at a crossroads between tw addventures,")
    print("\n one is the enchanted forest, the mystical and calm.")
    print("\n the other is the cyber city, futuristic and exciting.")

    options = {
        "1": "Enter teh Enchanted Forest",
        "2": "visit the cyber city",
    }
    path_choice = get_player_choice(options)

    if path_choice == "1":
        score = forest_path(name)
    else:
        score = city_path(name)
    return score

#This function shows the final result of the simulation\
#it takes both the player name and score and returns nothing

def show_results(name, score):
    print_divider()

    #print final score
    print(f"Adventure complete, {name}")
    print(f"Your final score is: {score} points")

    if score >= 30:
        print("Increadible! Great job")
    elif score >= 15:
        print("alright job! I'm kinda proud of you")
    else:
        print("You're kind of bad at this.")


    #end with a friendly message
    print("\n Thanks for playing loop quest simulation!")