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
print("")
name = input("What is your name?").strip().lower()
print("")

#---------
#stage 1
#---------
#strip() removes extra spaces and .lower() converts to lowercase

choice1 = input("You enter the primary loading bay. Go [left] towards vending machines or [right] to reception?").strip().lower()
print("")
if choice1 == "left":

#-----
#Stage 2a - left path decisions
#----
    choice2 = input("The vending machine has [candy] and [soda], what do you buy?").strip().lower()
    print("")
    if choice2 == "candy":

#stage 3a - candy bablandy
        choice3 = input("The candy gets stuck, do you [kick] the machine or [leave] it be?").strip().lower()
        if choice3 == "kick":
            print("")

            print("you kick the vending machine and it breaks, you are kicked off the station. You lose.")
        elif choice3 == "leave":
          print("")

          print("'you win this round, machine' you take the high road and leave the machine be. You feel proud of your maturity. You win.")
        else:
            print("")

            print("locked in a face off with the machine, neither of you want to act first. You stand there for the rest of the day. Your fate is unknown.")
    elif choice2 == "soda":
        print("")

        choice3b = input("The soda falls to the bottom of the machine. A man sitting next to you says that he is very thirsty and asks for your soda. Do you [give] soda or [refuse]?").strip().lower()
        if choice3b == "give":
                print("")

                print("the man thanks you and gives you a fancy looking watch. You win I guess")
        elif choice3b == "refuse":
                print("")

                print("'you greedy gripper!' The man shrivels up and dies. You... win?")
        else:
                print("")

                print("'it's a simple yes or no, kid. I'm dying over here' You do nothing and the old man shrivels up and dies. You lose")
    else:
        print("")

        print("torn with indecision, you do nothing. And nothing happens. You lose.")


elif choice1 == "right":

    choice2b = input("The receptionist asks if you have an appointment do you lie and say [yes] or tell the truth and say [no]").strip().lower()

    if choice2b == "yes":
        choice2ba = input("The receptionist asks for your name").strip().lower()
        print("")

        if "bill" in choice2ba or "keen" in choice2ba:
             print("'Ah, Mr. Keen, you're three days early. I guess that's space travel for you. I'll show you to your room.' You are taken to a lovely hotel room. In 2 days the real Bill Keen comes and you get in trouble. You lose") 
             print("")
        else:
             print("'You're not on the list, get out of here, loser.' You lose.")
             print("")
    elif choice2b == "no":
        choice2bb = input("'well, you're in luck. The next appointment is in 3 days. You may see the supreme space banker now.' You are taken to the supreme space banker. He asks what you want. Do you ask for a [loan] or a fleet of space [llamas]?").strip().lower()
        if choice2bb == "loan":
             print("The banker says 'well, it's hard times kid, but for you I think I could cut a deal.' You get a 38% APR loan to start your business. You win but actually you lose.")
             print("")
        elif choice2bb == "llamas":
             print("'You've got moxy, kid' says the space banker. 'The llamas are yours, you sly dog.' You become the galaxy's greatest llama farmer. You win")
             print("")

        else:
             print("You stand silent before the supreme space banker. He says, 'dude, what's up?' You say nothing. 'you're kinda freaking me out.' You say nothing. You are removed from the office. You lose")
             print("")

    else:
        print("You stand before the receptionist and say nothing. The receptionist says nothing. You enjoy a silent moment together. You win?")

else:
     print("I guess your adventure ends here. I guess the moral of the story is that you have to do something in order to have an adventure. You don't really lose but you certainly don't win.") 

