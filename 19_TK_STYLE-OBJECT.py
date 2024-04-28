import tkinter as tk
from tkinter import ttk
from tkinter import font

# setup
window = tk.Tk()
window.title("Styling")
window.geometry("400x300")

print(font.families())  # TO GET LIST OF AVAILABLE FONTS

'''
# style object
style = ttk.Style()
style.theme_use('classic')
print(style.theme_names())
# --> themes - ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
'''

# widgets
label = ttk.Label(master=window,
                  text="A LABEL\n And Now We Add ANother Line",
                  background="red",
                  foreground="white",
                  font=("Modern", 20),
                  justify="right")
label.pack()

style = ttk.Style()
style.configure('new.TButton', foreground="green", font=("Arabic Transparent", 10))  # Name of widgets start with T
style.map('new.TButton',
          foreground=[("pressed", "red"), ("disabled", "yellow")],
          background=[("pressed", "blue"), ("active", "blue")])  # active back/foreground

button = ttk.Button(master=window,
                   text="A BUTTON",
                    style='new.TButton')  # adding the style to the widget
button.pack()

# Run the window
window.mainloop()
