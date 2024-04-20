# DROP-DOWN-MENUS and NUMBER-SELECT-BOX-->
import tkinter as tk
from tkinter import ttk

# Create the window
window = tk.Tk()
window.geometry('600x400')
window.title('Combo and Spin')

################################################################################
# ################## DROP DOWN - combobox ######################################
################################################################################
items = ['ICECREAM', 'PIZZA', 'BROCCOLI']
food_string = tk.StringVar(value='SELECT FOOD')
combo = ttk.Combobox(window, textvariable=food_string)
combo.config(values=items)
combo.pack()

combo_label = ttk.Label(window, text="SELECTED ITEM", textvariable=food_string)
combo_label.pack()

# EVENTS FOR COMBOBOX
# '<<ComboboxSelected>>' -> special event for combobox
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text=f"Selected Food - {food_string.get()}"))


################################################################################
# ######################### SPIN BOX ###########################################
################################################################################
spin_string = tk.StringVar(value="NUMBER")
spin = ttk.Spinbox(window, from_=1, to=20, increment=2, textvariable=spin_string)
spin.pack()

spin.bind('<<Increment>>', lambda event: print('UP ARROW'))
spin.bind('<<DECREMENT>>', lambda event: print('DOWN ARROW'))

spin_label = ttk.Label(window, text="SELECTED VALUE", textvariable=spin_string)
spin_label.pack()

# Run the window
window.mainloop()
