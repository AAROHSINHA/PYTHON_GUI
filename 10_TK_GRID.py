import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Layout Intro')
window.geometry('600x400')

# widgets
label1 = ttk.Label(master=window, text="Label1", background='red', foreground="white")
label2 = ttk.Label(master=window, text="Label2", background='blue', foreground="white")

# grid
window.columnconfigure(index=0, weight=1)  # creates 1 column
window.columnconfigure(index=1, weight=1)  # creates 2nd column
window.columnconfigure(index=2, weight=2)  # creates 3rd column --> wider because of weight
window.rowconfigure(index=0, weight=1)
window.rowconfigure(index=1, weight=1)

label1.grid(row=0, column=1, sticky='nsew')  # stick - north-south-east-west
label2.grid(row=1, column=1, sticky='nsew', columnspan=2)  # widget spans 2 columns

# place

# Run the window
window.mainloop()
