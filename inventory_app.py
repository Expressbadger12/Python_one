#---------------------------
#simple inventory system using Python collections
#This program ussses a list to keep track of the item names
# a tuple to store menue options (they never change)
#Set  to track low-stock items
#usesess a dictionary to store item details (quantity and price)
# useses functions, loops, and IF/ELIF/ELSE for control flow
#---------------------------

#dictionary to hold our inventory
#key = item name (string)
#value = quantity and price
inventory = {
    "apple" : {"qty": 10, "price": 0.99},
    "banana" : {"qty": 5, "price": 0.59}
}

#list to keep an ordered list of item names
#this helps us print items in consistent order
item_names = list(inventory.keys())

#Tuple to store menu optoins not change
menu_options = (
    "1. View Inventory",
    "2. Add new item",
    "3. Update item quantity",
    "4. Mark item as low stock",
    "5. View low-stock items",
    "6. Quit"
)

low_stock_items = set()

#----------- HELPER FUNCTIONS

#Print the menu using our tuple 
#This function shows how we can LOOP over a TUPLE
def print_menu():
    print("\n=== Simple Inventory System")
    for option in menu_options:
        print(option)


#This function  will display all items in the inventory dictionary. shows how we loop through
#a ductionary useses a list for order
def view_inventory():
    if not inventory: #if the dictionary is empty
        print("\nInventory is empty")
        return

    print("\n--- Current Inventory ---")
    for name in item_names:
        details = inventory[name]
        qty = details["qty"]
        price = details["price"]
        #mark if item is low stock
        low_flag = "(LOW STOCK)" if name in low_stock_items else ""
        print(f" - {name.title()}: {qty} in stock at ${price: .2f}{low_flag}")


#this function add a new item to the inventory shows how we read intput and update our dictionary

def add_item():
    print("\n--- Add new item ---")
    name = input("Enter item name: ").strip().lower()

    #If the name is empty, we stop early
    if not name:
        print("Item name cannot be empty.")
        return
    
    #if item already exists we tell to update instead
    if name in inventory:
        print("Item already exists. Use 'update item quatnity' instead")
        return
    
    qty_str = input("enter starting wuantity: ").strip()
    price_str = input("enter item price:").strip()

    #use try/except to safely convert the strings to numbers
    try:
        qty = int(qty_str)
        price = float(price_str)
    except ValueError:
        print("quantity must be an integer and price must be a float")
        return
    
    inventory[name] = {"qty": qty, "price": price}

    #add the new name to our list of item names
    item_names.append(name)

    print(f"Added '{name}' with quantity {qty} and price ${price:.2f}.")

#This function changes the quantity of existing items
#
def update_quantity():
    print("\n---update item quantity---")
    name = input("Enter item name to update: ").strip().lower()

    if name not in inventory:
        print("That item does not exist in the inventory")
        return
    
    qty_str = input("enter new quantity: ").strip()

    try:
        new_qty = int(qty_str)
    except ValueError:
        print("Quantity must be an integer")
        return
    inventory[name]["qty"] = new_qty
    print(f"updated '{name}' quantity to {new_qty}.")

    #if wuantity is low(for example , <=3), add it to low)stock items set
    if new_qty <=3:
        low_stock_items.add(name)
        print(f"Note: '{name}' is now marked as low stock")
    else:
        #if wuantity is not low anymore remove from low stock itemss et
        if name in low_stock_items:
            low_stock_items.remove(name)
            print(f" '{name}' is no longer marked as low stock")

#this function manually marks an item as low stock

def mark_low_stock():
    print("\n---Mark item as low stock---")
    name = input("Enter item name to mark as low stock:").strip().lower()

    if name not in inventory: 
        print("That item does not exist in the inventory.")

    low_stock_items.add(name)
    print(f" '{name}' has been marked as low stock")

def view_low_stock_items():
    print("\n---Low stock items---")
    if not low_stock_items:
        print("No items are marked as low stock")
        return
    for name in low_stock_items:
        qty = inventory[name]["qty"]
        print(f"- {name.title()} (Qty: {qty})")

#--------------------------------


#main function that runs the program loop. Use WHile loop and if/elif/else to handle choice
def main():
    while True:
        print_menu()
        #ask the user for their choice

        choice = input("\nChoose an option (1-6): ").strip()

        #IF/ELIF/ELSE to handle each option
        if choice == "1":
            view_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_quantity()
        elif choice == "4":
            mark_low_stock()
        elif choice == "5":
            view_low_stock_items()
        elif choice == "6":
            print("Goodbue! Thanks for using the inventory system.")
            break
        else:
            print("Invalid choice. Please enter a nmber from 1 to 6")



    if __name__ == "__main__":
        main()


main()