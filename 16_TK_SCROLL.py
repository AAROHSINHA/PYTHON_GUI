##### CANVAS
import tkinter as tk
from tkinter import ttk
from random import randint, choice

# In Tkinter, there are 3 widgets that can be scrolled
# --> Canvas, Text and Treeview


# Setting the window
window = tk.Tk()
window.title("Scrolling")
window.geometry("600x400")

# canvas - scroll-region = [left, right, top, bottom]
canvas = tk.Canvas(master=window, background="white", scrollregion=(0, 0, 2000, 5000))
canvas.create_line(0, 0, 2000, 5000, fill="green", width="10")  # Creating a line from start to end

# Creating a couple of rectangles
for i in range(100):
    left = randint(0, 2000)
    top = randint(0, 5000)
    right = left + randint(10, 500)
    bottom = left + randint(10, 500)
    color = choice(("red", "green", "blue", "yellow", "orange"))
    canvas.create_rectangle(left, top, right, bottom, fill=color)  # left, top, right, bottom

# SCROLLBAR WIDGET
vertical_scrollbar = ttk.Scrollbar(master=window, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vertical_scrollbar.set)
vertical_scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")

horizontal_scrollbar = ttk.Scrollbar(master=window, orient="horizontal", command=canvas.xview)
canvas.configure(xscrollcommand=horizontal_scrollbar.set)
horizontal_scrollbar.place(relx=0, rely=1, relwidth=1, anchor="sw")

# scrollbar mousewheel scrolling
canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(2, "units"))  # amount, units
canvas.bind("<Control MouseWheel>", lambda event: canvas.xview_scroll(2, "units"))  # CTRL + SCROLL

canvas.pack(expand=True, fill="both")

# Mainloop
window.mainloop()


### ---> TEXT
import tkinter as tk
from tkinter import ttk
from random import randint, choice

# In Tkinter, there are 3 widgets that can be scrolled
# --> Canvas, Text and Treeview


# Setting the window
window = tk.Tk()
window.title("Scrolling")
window.geometry("600x400")

# TEXT
text = tk.Text(master=window)
# Filling the text
for i in range(1, 200):
    text.insert(f'{i}.0', f"text {i}\n")
text.pack(expand=True, fill="both")

scroll_bar_text = ttk.Scrollbar(master=window, orient="vertical", command=text.yview)
text.configure(yscrollcommand=scroll_bar_text.set)
scroll_bar_text.place(relx=1, rely=0, relheight=1, anchor="ne")

# Mainloop
window.mainloop()


