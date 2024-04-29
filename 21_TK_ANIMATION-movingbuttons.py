import random
import tkinter as tk
import customtkinter as ctk
from random import choice

def move_btn():
    global button_x
    global button_height
    button_height += 0.05
    button_x += 0.05
    button.place(relx=button_x, rely=0.5, relheight=button_height, anchor="center")
    print(button_x)

    # configure
    colors = ["red", "yellow", "pink", "orange", "purple", "magenta"]
    random_color = random.choice(colors)
    button.configure(fg_color=random_color, hover_color=random_color)


# WHEN USING ANIMATED WIDGETS, USE --> PLACE (More Efficient)
# window
window = ctk.CTk()
window.title("Animated Widgets")
window.geometry("600x400")

# button
button_x = 0.5
button_height = 0.1
button = ctk.CTkButton(master=window,
                       text="TOGGLE SLIDE-BAR",
                       command=move_btn)
button.place(relx=button_x, rely=0.5, relheight=button_height, anchor="center")

# run the window
window.mainloop()
