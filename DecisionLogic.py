
# 
# Decision logic activity adventure

# teaches:
# - Structured programming (sequence / selection / decision / iteration / loops)
# -expressions and operators (arithmetic, comparison, logical)
# -- If / elif / else
# - basis: writing tiny readable functions
# 
#print_line() prints a divider line to make the console output easier to read

def print_line(): #defines a simple helper function with no inputs
    #this function prints a visual divider 
    print("_" * 60) # multiplies the string _ by 60

print_line()

#-
#1) sequence: step by step intro + warm up math

print_line() # call our helper functio to draw a divider
print("Welcome to the Decision Logic Adventure!")
print("We'll explore operators, expressions, and conditional logic together")
print_line()

base_energy = 10 # assignment operation (=)
bonus_energy = 5 * 2 # mulitplication operator (*)
total_energy = base_energy + bonus_energy # addition operator (+)

print(f"Base Energ: {base_energy}") #f-string prints the variable nicly?
print(f"Bonus Energy: {bonus_energy}")
print(f"Total Energy: {total_energy}")
print_line()

#2) Input + validation (sequence) --> leads into decision (selection)

# ask the learner for their name using input() which will return a string

player_name = input("What's your name, adventurer? ")

player_name = player_name.strip() # cleans up the input
#Use strip() to remove extra spaces the user may accidentally add.

#if the user provided an empty name, repremend them

if player_name == "": #comparison operator (==)
    #selection: if the condition is true, run this block
    player_name == "Brave coder"
    print("very well, I'll pick a name for you") #let them know the default was used. 

print(f"Great to meet you, {player_name}")
print_line()

#-
#3) Operators and expressions

#Aritmetic operators
a = 9
b = 4
sum_ab = a + b
difference = a - b
product = a * b
truedivide = a / b
floordivide = a // b
remainder = a % b
power = a ** b

print("arithmatic examples")
print(f" {a} + {b} = {sum_ab}")
print(f"{a} / {b} = {truedivide}")
print(f"{a} // {b} = {floordivide}")

#comparison operators

x = 7
y = 10

print(" Comparison examples:")
print(f"{x} == {y} --> {x==y}") #false
print(f"{x} != {y} -> {x!= y}")
print(f" {x} > {y} {x > 7}")
print(f"{x} >= {7 } >= {x >= 7}")
print_line()

#logical operators

is_sunny = True
has_hat = False
print("logical examples:")
print(f"is_sunny and have_hat -> {is_sunny and has_hat}" ) #needs oth true conditions because and
print(f"is_sunny or have had -> {is_sunny or has_hat}") # has to have at least one
print(f"not has_hat -> {not has_hat}")

print_line()

#4 selection: if / elif / else

choice = input("choose a path (left/right/straight:): ").strip.lower()

if choice == "left":
    print("gone left and find merchant")
elif choice == "right":
    print("you go right and find a different, cooler merchange")
elif choice == "straight":
    print(" you get attacked by a clown>!?!")
else:
    print("you go around in circles")

#5 nested deciions 

# prompt the user about having a key and knowing the secret code
has_key_input = input("do you have the golden key? (y/n)").strip().lower()
knows_code_input = input("do you know the secret code? (y/n)").strip().lower()

has_kay = (has_key_input == "y") # true if user enters y
knows_code = (knows_code_input == "y")

if has_kay:
    
    if knows_code:
        print("Door opens! You enter the hall of knowledge") #if both conditions are true
    else: 
        print("the door does not open. You need the code") # has the key not the code
else:
    print("No key? The door wont budge")
print_line()



#6 wrap up

print("RECAP: You practiced......")
print(" - sequence: reading inputs, computing  values, printing results in order")
print(" - selection: if/else statements")
print(" - operators: arithmatic, comparison, logica, assignment")
print_line()

print(f"Nice work, {player_name}! Keep experiementing in vs code")