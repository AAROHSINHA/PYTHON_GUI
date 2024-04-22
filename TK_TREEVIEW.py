import tkinter as tk
from tkinter import ttk
import random

# Window
window = tk.Tk()
window.geometry('600x400')
window.title('TreeView')

# data
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thompson', 'Cook', 'Taylor', 'Walker', 'Clark']

# treeview
table = ttk.Treeview(master=window, columns=('FirstName', 'LastName', 'Emails'), show='headings')
table.heading('FirstName', text='FirstName')
table.heading('LastName', text='LastName')
table.heading('Emails', text='Emails')

# inserting values in table
table.insert(parent='', index=0, values=('John', 'Doe', 'JohnDoe@email.com'))

for i in range(100):
    first = first_names[random.randint(0, len(first_names) - 1)]
    last = last_names[random.randint(0, len(last_names) - 1)]
    email = first + last + '@email.com'
    table.insert(parent='', index=i, values=(first, last, email))

table.pack(fill='both', expand='true')

# run
window.mainloop()
