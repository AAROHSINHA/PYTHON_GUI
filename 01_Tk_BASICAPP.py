import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


def convert():
    mile_input = entry_integer.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)


# WINDOW
window = ttk.Window(themename= 'journal')
window.title('Demo')
window.geometry("300x150")


# title
title_label = ttk.Label(master=window, text="Miles To Kilometer", font='Calibri 24 bold')
title_label.pack()

# input field

# To store entry
entry_integer = tk.IntVar()

input_frame = ttk.Frame(master=window)
entry = ttk.Entry(master=input_frame, textvariable=entry_integer)
button = ttk.Button(master=input_frame, text="Convert", command=convert)

entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text="Output", font='Calibri 24', textvariable=output_string)
output_label.pack()

# RUN
window.mainloop()
