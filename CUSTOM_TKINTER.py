import customtkinter
import tkinter as tk
from tkinter import font
import customtkinter as ctk
from tkinter import messagebox


def button_command():
    messagebox.showinfo(title="MESSAGEBOX", message="THE INFO BOX WAS PRESSED")


def check_checkbox():
    pass


def combobox_callback(value):
    print("OPTION CLICKED = " + combobox_variable.get())


# STYLING MODULES --> External modules are very good to add styles.
# Window
window = ctk.CTk()  # This ctk window inherits from the tkinter window
window.title("CustomTkinter App")
window.geometry("600x400")

print(font.families())

# Widgets
label = ctk.CTkLabel(window, text="CTkLabel",
                     fg_color="red",
                     width=150,
                     height=40,
                     corner_radius=10,
                     font=("Impact", 20)
                     )  # anchor - nsew - position of image in label

button = ctk.CTkButton(master=window,
                       text="NEW BUTTON",
                       width=150,
                       height=30,
                       fg_color="white",
                       text_color="black",
                       border_width=2,
                       border_color="black",
                       border_spacing=5,
                       hover_color="black",
                       command=button_command)

checkbox = ctk.CTkCheckBox(master=window,
                           text="CTK_CHECKBOX",
                           checkbox_width=12,
                           checkbox_height=12,
                           border_width=2,
                           corner_radius=3,
                           fg_color="red",
                           hover_color="white",
                           text_color="white",
                           font=("TkSmallCaptionFont", 12),
                           onvalue=1,
                           offvalue=-1,
                           command=check_checkbox)

combobox_variable = customtkinter.StringVar(value="option2")
combobox = ctk.CTkComboBox(master=window,
                           values=["option 1", "option 2"],
                           command=combobox_callback,
                           variable=combobox_variable,
                           dropdown_fg_color="red",
                           dropdown_text_color="orange",
                           font=("Terminal", 15),
                           dropdown_font=("Script", 18))

entry = ctk.CTkEntry(master=window,
                     placeholder_text="Enter Text",
                     width=300,
                     height=30,
                     corner_radius=20,
                     text_color="red",
                     placeholder_text_color="black",
                     font=("Marlett", 14))

option = customtkinter.StringVar(value="option 1")
option_menu = ctk.CTkOptionMenu(master=window,
                                values=["option 1", "option 2", "option 3"],
                                variable=option,
                                command=lambda event: print(option.get()),
                                width=250,
                                button_color="black",
                                fg_color="white",
                                text_color="black",
                                font=("Arial CE", 20),
                                button_hover_color="white",
                                dropdown_fg_color="yellow",
                                dropdown_text_color="purple",
                                dropdown_font=("Courier", 15),
                                dropdown_hover_color="magenta")

progress_ = customtkinter.IntVar(value=0)
slider = ctk.CTkSlider(master=window,
                       from_=0,
                       to=100,
                       number_of_steps=10,
                       fg_color="red",
                       progress_color="black",
                       button_color="black",
                       variable=progress_,
                       command=lambda value: progress.stop())

progress = ctk.CTkProgressBar(master=window,
                              orientation="horizontal",
                              border_color="white",
                              border_width=3,
                              height=20,
                              progress_color="red",
                              variable=progress_
                              
                              )

label.pack()
button.pack(pady=10)
checkbox.pack(pady=10)
combobox.pack(pady=10)
entry.pack(pady=10)
option_menu.pack(pady=10)
slider.pack(pady=10)
progress.pack(pady=10)


# Run the window
window.mainloop()
