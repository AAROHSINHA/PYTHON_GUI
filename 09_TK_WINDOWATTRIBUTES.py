import tkinter as tk
from tkinter import ttk

# Create window
window = tk.Tk()
window.geometry('600x400+630+0')  # '600x400+left+top'
window.title('More on the window')

# Minimum window size
window.minsize(200, 100)
# window.maxsize(800, 700)
window.resizable(True, False)  # x=True, y=False

# screen sized
print(window.winfo_screen())  # Method to return the width of screen
print(window.winfo_screenheight())
print(window.winfo_screenwidth())

# window attributes
window.attributes('-alpha', 1)  # alpha, transparency
window.attributes('-topmost', True)  # window will be always at top of other background apps

'''
# security event
window.bind('<Escape>', lambda event: window.quit())
window.bind('-disable', True)  # you wont be able to close the window until ESC, title bar is disabled
window.bind('-fullscreen', True)
'''

'''
# title bar
window.overrideredirect(True)  # title bar disappears
'''


# Run the window
window.mainloop()

