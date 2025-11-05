##########################################
#TIME MACHINE JOURNAL
#Purpose:
# 1) practice variables, input / output, and file reading / writing
# 2) demonstrates text file creation and persistence between runs

"""
================================================================
This program demonstrates basic Python I/O (input / output) and how to save user data in a text file
================================================================
"""
 
#step 1: display a welcome message to the user
print("============================================")
print("           TIME MACHINE JOURNAL             ")
print("--------------------------------------------")
print("You can record journal entries that are saved between uses.")
print("Each entry includes your name, year, and experience. \n")

# step 2:  Collect user input (different data types)
# string variable - stores a user's name as text
name = input("What is your name, traveler?")

# Integer variable = stores the numeric values 
year = int(input("What is the year: "))

#Float variable = stores decimal values
rating = float(input("How would you rate this trip from 0.0 to 5.0"))

# Another string variable - user enters a journal entry
entry = input("Write your journal entry: ")

# Step 3: write data to a text file
#'a' means append mode (adds data without earasing previous entries)
# encoding = 'UTF-8' allows special characters and emojis to be saved properly
with open("journal.txt", "a", encoding="utf-8") as f:
    f.write(f'Name: {name} | Year: {year} | Rating: {rating:.1f} | Entry: {entry}\n')

# confirmation message
print("\n Your entry has been saved to 'journal.txt'.")

# step 4: ask if the user wants to read previous entries
see_entries = input("Would you like to read your past journal entries? (y/n) ").lower()

#if the user types "y", open the file and display contents

if see_entries == 'y':
    try:
        #Open file read mode ('r') and display all text
        with open("journal.txt", "r", encoding="utf-8") as f:
            history = f.read()
            print("\n---PAST ENTRIES---\n")
            print(history)
            print("---------------------")
    except FileNotFoundError:
        #This will run if the file doesn't exist yet
        print("No journal file found -- make an entry first")

