#--------------------------------------------------
#Python loops and functions
#Numbrt guessing game
#--------------------------------------------------

# we need to import a module/library to generate a number
import random
#--------------------------------------------------

#Function: greet_player
#purpose: print a welcome message to the user
#input: playername string
#returns: none
#-------------------------------------------------
def greet_player(player_name):
    #us a f-string to include the players name in thes tring
    print(f"\nWelcome, {player_name}!")
    print("\nwe're going to play a number guessing game.")
    print("\nTry to guess the number in as few tries as possible.\n")

#---------------------------------------------------------
#function: get secret number
#purpose: generate and return a random number
#inputs# none
#return: secret number (int)
#-----------------------------------------------------------
def get_secret_number():
    secret_number = random.randint(1,20) #returns a random integure between 1 and 20 ()inclusive
    return secret_number

#----------------------------------------------------------


#---------------------------------------------------------------------
#play round
#purpose: to play one round fot eh guessing game
# inoyt]: round_number int
#returns: number of guesses int is/] fa
def play_round(round_number):
        print(f"\n==== ROUND {round_number}====")

        secret_number = get_secret_number()
        max_guesses = 5
        guesses_used = 0

        while guesses_used < max_guesses:
            guess = int(input("Enter your guess(1 tp 20): "))

            guesses_used += 1

            if guess == secret_number:
                 print(" Correct! You entetred the secret number!")
                 print(f"You used {guesses_used} guesses.")
                 return guesses_used
        
            elif guess < secret_number:
                 print("Too low a number, go highterr")

            else:
                 print("Too hight, try a lower njumber!")        

            if guesses_used < max_guesses:
                 print (f" You have {guesses_used - max_guesses} guesses left!\n")

        print("\n out of guesses! \n")
        print(f"The number was: {secret_number}")
        return None

#-----------------
#function: show_sumary
#purpose: show a summer of how the player did accross all rounds

#-----
def show_summary(results_list):
    print("\n===== Game Summary =====")

     #use a fore loop to go through each round results
     #enumerate gives us both the index (round number) and value (guesses used)
    for index, guesses_used in enumerate(results_list, start=1):
          #if guesses_used is None, the player did not guess correctly that round
        if guesses_used is None: #or == 0
            print(f"Round {index}: Did not guess correctly")
        else:
            print(f"Round {index}: Guessed correctly in {guesses_used} guess(es).")
    #optionally we can calculate how many rounds were successful
    successful_rounds = 0 

    for guesses_used in results_list:
         if guesses_used is not None:
              successful_rounds += 1
    print(f"\nYou guessed correctly in {successful_rounds} out of {len(results_list)} round(s).")


#----------------------------
#Main function
#Purpose rus the whole program

def main():
    player_name = input("What is your name? ")

    #call our greet_player function
    greet_player(player_name)

    # ask how many rounds they want to play
    total_rounds = int(input("How many rounds would you like to play?"))

    #create an empty list to store the results for each round
    round_results = []
    
    #use a for loop to play multiple rounds
    #range(total_rounds) will loop from 0 up to total_rounds - 1
    #we add 1 to show round numbers starting at 1
    for round_number in range(1, total_rounds + 1):
         #call play rounds and capture the result
        result = play_round(round_number)

        # append the result of the round to our result list
        round_results.append(result)

        print("\n--------------------------------------")

    #after all rounds are played, show a summery using our function
    show_summary(round_results)

    print("\n Thank you for playing!")

#--------------------------------------------------------------------
# This line makes sure main()runs when the file is executed directly and not when it is imported as a module

if __name__ == "__main__":
     main()