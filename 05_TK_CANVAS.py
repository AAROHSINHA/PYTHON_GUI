import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')

# canvas
canvas = tk.Canvas(master=window, bg='white')
canvas.pack()


# Creating a rectangle [(left, top, right, bottom), fill=color, border-width, other_arguments____]
canvas.create_rectangle((50, 20, 100, 200), fill='red', width=10, dash=(3, 2, 1, 1), outline='yellow')
canvas.create_line((0, 0, 100, 150), fill='blue', width=6)  # [(start_x, start_y, end_x, end_y), color, width]
canvas.create_oval((150, 150, 250, 250), fill='green', width=10, outline='red')
canvas.create_polygon((15, 20, 100, 200, 350, 50), fill='white', width=5, outline='black')
canvas.create_arc((150, 150, 250, 250), outline='yellow', fill='yellow', start=220)
# arc with same dimensions of oval to fit in it


# Create text
canvas.create_text((100, 200), text='This is some text', fill='green', width=10)

# Creatign a window
canvas.create_window((50, 100), window=ttk.Label(master = window, text='This is text in a canvas'))
canvas.create_window((50, 150), window=ttk.Button(master = window, text='This is text in a canvas'))


# Run Window
window.mainloop()
