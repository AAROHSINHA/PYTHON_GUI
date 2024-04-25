import tkinter as tk
from tkinter import ttk

# Creating a window
window = tk.Tk()
window.title("WIDGET SIZES")
window.geometry('400x300')

# widget.lift() --> widget comes on top of all widgets
# widget.lower() --> widget goes to bottom of all widgets

# WIDGETS
label1 = ttk.Label(window, text="Label1", background="green", foreground="white")
label2 = ttk.Label(window, text="Label2", background="red", foreground="white")

button1 = ttk.Button(window, text='raise label 1', command= lambda: label1.lift(aboveThis=label2))
button2 = ttk.Button(window, text='raise label 2', command=lambda: label2.lift())

# layout
label1.place(x=50, y=100, width=200, height=150)
label2.place(x=150, y=60, width=40, height=100)

button1.place(rely=1, relx=0.8, anchor='se')
button2.place(rely=1, relx=1, anchor='se')

# Running the window
window.mainloop()
