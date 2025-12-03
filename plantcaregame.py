#------- 
import tkinter as tk

class Plant:
    def __init__(self, name: str):
        self.name = name

        self._water = 5 #water level 0-10
        self._sun = 5 
        self._health = 5

    def water_plant(self):
        self._water += 1
        if self._water > 10:
            self._water = 10

        #if water is in a good range, health goes up a little
        if 4 <= self._water <= 8: 
            self._health += 1
        else:
            self._health -= 1
            self._clamp_stats()

    def give_sun(self):
        self._sun += 1
        if self._sun > 10:
            self._sun = 10

        if 4 <= self._sun <= 8:
            self._health += 1
        else:
            self._health -= 1

        self._clamp_stats()

    def skip_day(self):
        #water and sun slowly go down
        self._water -= 1
        self._sun -= 1
        #losing too much water or sun hurts the health

        if self._water < 3 or self._sun < 3:
            self._health -= 1

        self._clamp_stats()

    def reset(self):
        self._water = 5
        self._sun = 5
        self._health = 5

    def _clamp_stats(self):
        if self._water < 0:
            self._water = 0
        if self._water > 10:
            self._water = 10
        
        if self._sun < 0:
            self._sun = 0
        if self._sun > 10:
            self._sun = 10

        if self._health < 0:
            self._health = 0
        if self._health > 10:
            self._health = 10

    def get_status_text(self) -> str:
        if self._health >= 8:
            mood = "Thriving!"
        elif self._health >=5:
            mood = "Doing okay."
        elif self._health >= 3:
            mood = "wilting"
        else:
            mood = "Dying"

        status = (
            f"Plant: {self.name}\n"
            f"Water: {self._water}/10\n"
            f"Sun: {self._sun}/10\n"
            f"Health: {self._health}/10\n"
            f"Status: {mood}"
        )
        return status

    def is_dead(self) -> bool:
        return self._health == 0 #the plant is dead
        
#------------

class PlantGameGUI:
    def __init__(self, root: tk.Tk):
        self.root = root

        self.root.title("Virtual Plant Care Game")

        self.plant = Plant("Sunny")

        #create lables and buttons and stuff
        self.title_label = tk.Label(
            self.root,
            text = "Welcome to the Virtual Plant Care",
            font = ("Times New Roman", 16, "bold")
        )
        self.title_label.pack(pady = 10)

        self.instructions_label = tk.Label(
            self.root,
            text="Click the buttons below to care for your plant",
            font = ("Times New Roman", 11)
        )
        self.instructions_label.pack(pady=5)

        self.status_label = tk.Label(
            self.root,
            text=self.plant.get_status_text(),
            font=("Consolas", 11),
            justify="left",
            borderwidth=2,
            relief="groove",
            padx=10,
            pady=10
        )
        self.status_label.pack(pady=10)

        #Frame to group the action buttons in a row
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=5)
        
        self.water_button = tk.Button(
            self.button_frame,
            text="water plant",
            font=("Arial", 11),
            command=self.handle_water_click
        )
        self.water_button.grid(row=0, column=0, padx=5, pady=5)

        self.sun_button = tk.Button(
            self.button_frame,
            text="Give sun",
            font=("Arial", 11),
            command=self.handle_sun_click
        )
        self.sun_button.grid(row=0, column=1, padx=5, pady=5)

        self.skip_button = tk.Button(
            self.button_frame,
            text="Skip day",
            font=("arial", 11),
            command=self.handle_skip_day
        )
        self.skip_button.grid(row=0, column=2, padx=5, pady=5)

        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(pady=10)

        self.reset_button = tk.Button(
            self.control_frame,
            text="Reset Plant",
            font=("Arial", 11),
            command=self.handle_reset
        )
        self.reset_button.grid(row=0, column=0, padx=5)

        self.quit_button = tk.Button(
            self.control_frame,
            text="Quit game",
            font=("Arial", 10),
            command=self.root.quit
        )
        self.quit_button.grid(row=0, column=1, padx=5)

        #Message label to show the short feedback after action
        self.message_label = tk.Label(
            self.root,
            text="Tip: Keep water and sun between 4 and 8 for best health",
            font=("Arial", 10, "italic"),
            fg="gray"
        )
        self.message_label.pack(pady=5)

    def handle_water_click(self):

        if not self.plant.is_dead():
            self.plant.water_plant()
            self.update_display(message="You watered the plant.")
        else:
            self.update_display(message="Your plant is already dead... reset to try agian")

    def handle_sun_click(self):
        if not self.plant.is_dead():
            self.plant.give_sun()
            self.update_display(message="You moved the plant into the sun")
        else:
            self.update_display(message="Your plant is already dead... reset to start over")

    def handle_skip_day(self):
        if not self.plant.is_dead():
            self.plant.skip_day()
            self.update_display(message="Time has passed")
        else:
            self.update_display(message="Time has run out for this plant... try reseiting")

    def handle_reset(self):
        self.plant.reset()
        self.update_display(message="New plant! Take good care of this one!")

#----------------------------------------------------------------------------

    def update_display(self, message: str):
        self.status_label.config(text=self.plant.get_status_text())

        if self.plant.is_dead():
            self.message_label.config(
                text="Oh no! Your plant has died. Click 'reset' to reset",
            )
        else:
            self.message_label.config(text=message, fg="gray")

#-----
if __name__ == "__main__":
    root = tk.Tk()

    app = PlantGameGUI(root)

    root.mainloop()


