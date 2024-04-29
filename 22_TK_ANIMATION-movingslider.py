import random
import tkinter as tk
import customtkinter as ctk
from random import choice


class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(parent)

        # general attributes
        self.start_pos = start_pos + 0.02
        self.end_pos = end_pos
        self.width = abs(start_pos - end_pos)

        # animation logic
        self.pos = self.start_pos
        self.in_start_pos = True  # tracks if the widget is in start position or not

        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width, relheight=0.9)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backward()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backward(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_backward)
        else:
            self.in_start_pos = True


# WHEN USING ANIMATED WIDGETS, USE --> PLACE (More Efficient)
# WINDOW.AFTER(1000, func)  means run the function after specified time
# window
window = ctk.CTk()
window.title("Animated Widgets")
window.geometry("600x400")

# animated widget
animated_panel = SlidePanel(parent=window, start_pos=0, end_pos=-0.3)  # THIS IS A FRAME. WE CAN ADD ANY LABEL ETC.
ctk.CTkButton(animated_panel, text="Label 1").pack(expand=True, fill="both", padx=3, pady=3)
ctk.CTkButton(animated_panel, text="Label 1").pack(expand=True, fill="both", padx=3, pady=3)
ctk.CTkButton(animated_panel, text="Label 1").pack(expand=True, fill="both", padx=3, pady=3)
ctk.CTkTextbox(animated_panel, fg_color=('#dbdbdb', '#2b2b2b')).pack(expand=True, fill="both")

# button
button_x = 0.5
button_height = 0.1
button = ctk.CTkButton(master=window,
                       text="TOGGLE SLIDE-BAR",
                       command=animated_panel.animate)
button.place(relx=button_x, rely=0.5, relheight=button_height, anchor="center")

# run the window
window.mainloop()
