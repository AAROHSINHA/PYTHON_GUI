import tkinter as tk
from tkinter import ttk

# Creating the window
window = tk.Tk()
window.title("buttons")
window.geometry("600x400")


# BUTTON -->
def button_func():
    print("a basic button")


button_string = tk.StringVar(value='Button With StringVar')
button = ttk.Button(master=window, text='A simple button', command=button_func, textvariable=button_string)
button.pack()


# CHECKBUTTON -->
check_var = tk.IntVar(value=10)  # 1 - checked 0 - unchecked
check = ttk.Checkbutton(master=window, text='CheckBox 1', command= lambda : print(check_var.get()),
                        variable=check_var,
                        onvalue=10,
                        offvalue=5)
check.pack()


# RADIOBUTTON -->
# each must have "VALUE", or else all start to function together
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window, text="RadioButton1", value='radio 1',
                         variable=radio_var,
                         command=lambda:print(radio_var.get()))
radio2 = ttk.Radiobutton(window, text="RadioButton2", value='radio 2',
                         variable=radio_var,
                         command=lambda:print(radio_var.get()))
radio1.pack()
radio2.pack()

# Running the window
window.mainloop()
