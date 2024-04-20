import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'x : {event.x}  y : {event.y}')

# window
window = tk.Tk()
window.geometry('600x500')
window.title('Event Binding')

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text='A Button')
button.pack()

# EVENT 1 -- ALT + A - print something
# --> window.bind('<modifier-type-detail>', function)
window.bind('<Alt-KeyPress-a>', lambda event: print('An event'))
button.bind('<Alt-KeyPress-w>', lambda event: print('btn event'))  # only works when button selected

# EVENT 2 --> Motion
entry.bind('<Motion>', get_pos)  # we get position of mouse on text widget (on all window wif window.bind() was used)

# EVENT 3 - Any kind of keypress
window.bind('<KeyPress>', lambda event: print(f'a button was pressed - {event.char}'))

# EVENT 4 - selecting entry field
entry.bind('<FocusIn>', lambda event: print('entry field was selected'))  # works when we select it
entry.bind('<FocusOut>', lambda event: print('entry field was unselected'))

# Run the window
window.mainloop()

