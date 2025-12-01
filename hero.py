#--------------------------
#Hero simulator 
#OOP

import tkinter as tk

#--------
# Create base class
class Character:

    def __init__(self, name):
        #store name
        self.name = name

    #_health is encapsulated (protected)
        self.health = 100

    def basic_attack(self):
        return f"{self.name} performs a basic attack!"
    
#---------------------------------------
#Create child classes(Inheritance)

#Wizard is a child of character, so it inherits everythign from character
class Wizard(Character):
    # a special move unique to wizard
    def special(self):
        return f"{self.name} casts a blazing Fireball!"
    
class Warrior(Character):
    # A special character 
    def special(self):
        return f"{self.name} unleases a mighty power strike!"
    
#------
# Build the GUI

class HeroGUI:
    def __init__(self, root):

        # Create a hero 
        # You can change wizard --> warrior if you want
        self.hero = Wizard("Astra")

        self.label = tk.Label(root, text="Choose an action for your hero:")
        self.label.pack()

        self.basic_btn = tk.Button(
            root,
            text="Basic Attack",
            command=self.do_basic
        )
        self.basic_btn.pack()

        # Button for the special attack
        self.special_btn = tk.Button(
            root,
            text="Special Attack",
            command=self.do_special
        )
        self.special_btn.pack()

        # output area - displays result on the screen

        self.out = tk.Label(root, text="", font=("Arial, 12"))
        self.out.pack()

    #-------------------
    #Event handlers

    def do_basic(self):
        self.output.config(text=self.hero.basic_attack())

        # Respond to special

    def do_special(self):
        self.output.config(text=self.hero.special())

#-----------
# Part 5

root = tk.Tk()

root.title("Hero simulator lite")

# create an instance of gui applicatio
app = HeroGUI(root)

root.mainloop()

