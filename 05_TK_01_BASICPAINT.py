# CREATING A BASIC PAINT APP
import tkinter as tk
from tkinter import ttk

# Create window
window = tk.Tk()
window.geometry('600x500')
window.title('Canvas')

canvas = tk.Canvas(window, bg='white')
canvas.pack()

# Event - checking the movement of the mouse
def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brush_size/2, y - brush_size/2, x + brush_size/2, y + brush_size/2), fill='black')


brush_size = 10
canvas.bind('<Motion>', draw_on_canvas)

# Checking mousewheel
def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4

    brush_size = max(0, min(brush_size, 50))

canvas.bind('<MouseWheel>', brush_size_adjust)


# Run the window
window.mainloop()
