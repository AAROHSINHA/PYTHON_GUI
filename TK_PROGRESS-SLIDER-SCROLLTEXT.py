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


# Run the window
window.mainloop()


