import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Create window
window = tk.Tk()
window.title('PROGRESSBAR AND SLIDER')

# Slider --> Can be moved by the user
# Progressbar --> cannot be set by user, rather used to progress

# SLIDER
scale_int = tk.IntVar(value=15)

horizontal_slider = ttk.Scale(master=window, command=lambda value: progress.stop(), from_=0, to=25, length=300,
                              orient='vertical', variable=scale_int)
horizontal_slider.pack()

vertical_slider = ttk.Scale(master=window, command=lambda value: print('test2'), from_=100,to=200, length=50,
                             orient='vertical')
vertical_slider.pack()


# PROGRESS BAR
progress = ttk.Progressbar(master=window, variable=scale_int, maximum=25, length=400)
progress.pack()

# start
progress.start(3000)  # Progressbar starts by itself
# 3000 - starts after 3000 ms = 3 s


# ScrolledText
scrolled_text = scrolledtext.ScrolledText(window, width=100, height=5)
scrolled_text.pack()


##########################################################
###### EXCERSISE
##########################################################
import tkinter as tk
from tkinter import ttk


# Run the window
window = tk.Tk()
window.title('SCROLLBAR PROGRESSBAR')
window.geometry('600x500')

# Scrollbar
scroll_int = tk.IntVar(value=0)
scrollbar = ttk.Scale(master=window, from_=0, to=100, length=300, orient='vertical', variable=scroll_int,
                      command=lambda event: print(scroll_int.get()))
scrollbar.pack()

# Progressbar
progressbar = ttk.Progressbar(master=window, length=500, variable=scroll_int)
progressbar.start()
progressbar.pack()

label = ttk.Label(window, textvariable=scroll_int)
label.pack()

window.mainloop()




# Run the window
window.mainloop()


