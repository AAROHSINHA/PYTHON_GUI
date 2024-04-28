import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def ask_yes_no():
    # messagebox.showerror(message="ERROR")
    # messagebox.showinfo(title="INFO TITLE", message="info")
    messagebox.askquestion(title="Quesiton", message="Are You Ready")  # returns the answer


def create_window():
    global extra_window
    extra_window = tk.Toplevel()
    extra_window.geometry("300x400")
    ttk.Label(extra_window, text="EXTRA WINDOW").pack()
    ttk.Button(extra_window, text=" A button").pack()
    ttk.Label(extra_window, text="Another Label").pack(expand=True)



# setup
window = tk.Tk()
window.title("Multiple windows")
window.geometry("600x400")

button1 = ttk.Button(window, text="open main window", command=create_window)
button1.pack(expand=True)

button2 = ttk.Button(window, text="close main window", command=close_window())
button2.pack(expand=True)

button3 = ttk.Button(window, text="create yes no window", command=ask_yes_no)
button3.pack(expand=True)


# Run the window
window.mainloop()

