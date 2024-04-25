import tkinter as tk
from tkinter import ttk

# Creating a window
window = tk.Tk()
window.title("HIDE WIDGEST")
window.geometry('600x400')

#########################################################################
#########################################################################
#########################################################################
# PLACE -->


def toggle_label_place():
    global label_visibility
    if label_visibility:
        label.place_forget()
        label_visibility = False
    else:
        label_visibility = True
        label.place(relx=0.5, rely=0.5, anchor="center")


# place
button = ttk.Button(master=window, text='TOGGLE LABEL', command=toggle_label_place)
button.place(x=10, y=10)

label_visibility = True
label = ttk.Label(window, text="A Label")
label.place(relx=0.5, rely=0.5, anchor="center")


#########################################################################
#########################################################################
#########################################################################
# GRID -->
def toggle_label_grid():
    global label_visibility
    if label_visibility:
        label.grid_forget()
        label_visibility = False
    else:
        label_visibility = True
        label.grid(column=1, row=0)


# GRID -->
window.columnconfigure(index=0, weight=1, uniform='a')
window.columnconfigure(index=1, weight=1, uniform='a')
window.rowconfigure(index=0, weight=1, uniform='a')

button = ttk.Button(master=window, text='TOGGLE LABEL',  command=toggle_label_grid)
button.grid(column=0, row=0)

label_visibility = True
label = ttk.Label(window, text="A Label")
label.grid(column=1, row=0)



# Running the window
window.mainloop()
