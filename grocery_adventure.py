# Concepts here: lists, tuples, dictionaries

#------------------------------------------

#This tuple stores basic store information
#Tuple are like lists, but they cannot be changed
store_info = ("Grocery Adventure", "123 Python Lane")

#print a simple welcome message using values from tuple
print("Welcome to ", store_info[0])
print("Location:", store_info[1])
print("-----------------------------------")

# a list of items the store sells
#LIsts are ordered and can be changed (add /remove items)
store_items = ["apple", "bananas", "bread", "milk", "eggs"]

# a dictionary that maps each item to a price
#dictionary stores data as key:value pairs
# key --> item name (string)
# value --> price (number)

store_prices = {
    "apple" : 0.75,
    "bananas" : 0.50,
    "bread" : 2.50,
    "milk" : 3.00,
    "eggs" : 40.00
}

# This list will hold the items that the user chooses to buy
shopping_cart = [] #starts empty

def show_menu(): #this function prints the main menu / functions help us reuse code
    print("\nWhat would you like to do?")
    print("\n1 - view store items")
    print("\n2 - add items to cart")
    print("\n3 - view cart and total")
    print("\n4 - quit game")

def show_store_items():
    print("\n--- Store Items ---")
    #We loop through each item in the list
    for item in store_items:
        price = store_prices[item]
        print(f"{item} : ${price: .2f}")

def add_to_cart():
    item = input("\nType the name of the item to add: ").strip().lower()

    #Check if the item is in the store items list
    if item in store_items:
        shopping_cart.append(item)
        print(f"{item} has been added to your cart!")
    else:
        # if it doesn't exist, show a message
        print("Sorry, that item is not in the store.")

def view_cart_and_total():
    print("\n--- Your cart  ---")
    # if the cart is empty, tell the user and return early
    if len(shopping_cart) == 0:
        print("Your cart is empty")
        return # exit the function here
    
    #create a dictionary to count how many of each item the user has
    #Example: {"apple" : 2,}
    item_counts = {}
    for item in shopping_cart:
        if item not in item_counts:
            item_counts[item] = 1
        else:
            item_counts[item] += 1
    
    total_cost = 0

    for item, count in item_counts.items():
        price = store_prices[item]
        #calculate subtotal for this item (price * quantity)
        subtotal = price * count

        total_cost += subtotal
        print(f"{item} x {count} = ${subtotal: .2f}")

    # after the loop, print total cost
    print("--------------------------------------")
    print(f"total cost: ${total_cost: .2f}")

#------------------------------------------main game loop--------------------------------------------------
running = True

while running:
    show_menu()

    choice = input("enter your choice, (1-4):").strip()

    if choice == "1":
        show_store_items()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        view_cart_and_total()
    elif choice == "4":
        running = False
    else:
        print("Invalid cjoice please enter 1, 2, 3, or 4")