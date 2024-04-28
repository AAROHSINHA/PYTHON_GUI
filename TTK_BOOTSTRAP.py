import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


# window
window = ttk.Window(themename='journal')  # darkly, journal
window.title("ttk bootstrap intro")
window.geometry("400x300")

label = ttk.Label(window, text="Label", bootstyle="info")
label.pack(pady=10)

button1 = ttk.Button(window, text="Button 1", bootstyle="info")
button1.pack(pady=10)

button2 = ttk.Button(window, text="Button 2", bootstyle="dark-outline")
button2.pack(pady=10)

button3 = ttk.Button(window, text="Button 3", bootstyle="success")
button3.pack(pady=10)


# run
window.mainloop()
