#######################
# Title: Working title
# Author: Boone Stewart
# Description: text based adventure simulation game. 
###############
#How to play:
#Read the story and type one of the options shown in [brackets].
#press enter after typing your choise
#each choice leads to a new situation or an ending
#There are at least three decision stages in this game
################

#--------------------------------
#Stage 0 - intro
#---------
print("Welcome to space station 7!")

#---------
#stage 1
#---------
#strip() removes extra spaces and .lower() converts to lowercase

choice1 = input("You enter the primary loading bay. Go [left] towards vending machines or [right] to reception?").strip().lower()

if choice1 == "left":

#-----
#Stage 2a - left path decisions
#----
    choice2 = input("The vending machine has [candy] and [soda], what do you buy?").strip().lower()

    if choice2 == "candy":

#stage 3a - candy bablandy
        choice3 = input("The candy gets stuck, do you [kick] the machine or [leave] it be?").strip().lower()

        if choice3 == "kick":
            print("you kick the vending machine and it breaks, you are kicked off the station")
        elif choice3 == "leave":
          print("'you win this round, machine' you take the high road and leave the machine be. You feel proud of your maturity")
        else:
            print("locked in a face off with the machine, neither of you want to act first. You stand there for the rest of the day")
    elif choice2 == "soda":
        choice3b = input("The soda falls to the bottom of the machine. A man sitting next to you says that he is very thirsty and asks for your soda. Do you [give] soda or [refuse]?")
        if choice3b == "give":
                print("the man thanks you and gives you a fancy looking watch. You win I guess")
        elif choice3b == "refuse":
                print("'you greedy gripper!' The man shrivels up and dies. You... win?")
        else:
                print("'it's a simple yes or no, kid. I'm dying over here' You do nothing and the old man shrivels up and dies. You lose")
    else:
        print("torn with indecision, you do nothing.")


elif choice1 == "right":

    choice2b = input("The receptionist asks if you have an appointment do you lie and say [yes] or tell the truth and say [no]")

    if choice2b == "yes":
        print("")
    elif choice2b == "no":
        print("")
    else:
        print("")
#stage 3b 

