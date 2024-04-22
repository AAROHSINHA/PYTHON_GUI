import tkinter as tk
from tkinter import ttk

# Create the window
window = tk.Tk()
window.title('MENUS')
window.geometry('600x400')

# menu
menu = tk.Menu(master=window)

# sub menu
file_menu = tk.Menu(master=menu, tearoff=False)  # First sub menu - FILE
# adding options/menu to FILE
file_menu.add_command(label='NewFile', command=lambda: print("New File"))
file_menu.add_command(label='OpenFile', command=lambda: print("Open Files"))
file_menu.add_separator()  # adds that seperator line in the menu
file_menu.add_command(label="SaveFile", command=lambda: print("Save Files"))
menu.add_cascade(label='FILE', menu=file_menu)

# another sub menu
help_menu = tk.Menu(master=window, tearoff=False)  # Second sub menu - HELP
# adding options/menu to FILE
help_menu.add_command(label='FAQ', command=lambda: print(help_check_string.get()))
help_menu.add_separator()
help_check_string = tk.StringVar()
help_menu.add_checkbutton(label='Check', onvalue='on', offvalue='off', variable=help_check_string)
menu.add_cascade(label='HELP', menu=help_menu)

# MENU INSIDE MENU
exercise_menu = tk.Menu(menu, tearoff=False)
exercise_menu.add_command(label='EXERCISE TEXT 1')
menu.add_cascade(label='EXERCISE', menu=exercise_menu)

# adding a sub menu in the menu item
exercise_sub_menu = tk.Menu(menu, tearoff=False)
exercise_menu.add_cascade(label='MORE STUFF', menu=exercise_sub_menu)

exercise_sub_menu.add_command(label='entry1')
exercise_sub_menu.add_command(label='entry2')
exercise_sub_menu.add_command(label='entry3')


window.config(menu=menu)

######################################################################################
######################################################################################
######################################################################################

# menu button - MORE OPTIONS
menu_button = ttk.Menubutton(master=window, text='Menu Button')
menu_button.pack()

button_sub_menu = tk.Menu(master=menu_button,tearoff=False)
# ENTRY 1
button_sub_menu.add_command(label='ENTRY 1', command=lambda: print("TEXT 1"))
button_sub_menu.add_separator()
button_sub_menu.add_command(label='ENTRY 2', command=lambda: print("TEXT 2"))

menu_button.config(menu=button_sub_menu)

# Run the window
window.mainloop()
