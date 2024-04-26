import tkinter as tk
from tkinter import ttk


# App is going to be the main window which inherits from tk.Tk
class App(tk.Tk):
    def __init__(self, title, size):

        # main setup
        super().__init__()
        self.title(title)  # setting the title with arguments
        self.geometry(f"{size[0]}x{size[1]}")  # setting the dimension with arguments
        self.minsize(size[0], size[1])

        # widgets
        self.menu = Menu(self)  # parent here is self (APP --> tk.Tk)
        self.main_ = Main(self)

        self.mainloop()  # running the window

# Creating the Frame 1 (MENU)
class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(x=0, y=0, relwidth=0.3, relheight=1)  # placing self
        self.create_widgets()

    # --> METHOD TO CREATE THE WIDGETS
    def create_widgets(self):

        # create the widgets
        menu_button1 = ttk.Button(master=self, text="Button 1")
        menu_button2 = ttk.Button(master=self, text="Button 2")
        menu_button3 = ttk.Button(master=self, text="Button 3")

        menu_slider1 = ttk.Scale(master=self, orient="vertical")
        menu_slider2 = ttk.Scale(master=self, orient="vertical")

        toggle_frame = ttk.Frame(master=self)

        menu_toggle1 = ttk.Checkbutton(master=toggle_frame, text="Check 1")
        menu_toggle2 = ttk.Checkbutton(master=toggle_frame, text="Check 2")

        entry = ttk.Entry(master=self)

        # greate the grids
        self.columnconfigure(index=0, weight=1, uniform="a")
        self.columnconfigure(index=1, weight=1, uniform="a")
        self.columnconfigure(index=2, weight=1, uniform="a")
        self.rowconfigure(index=0, weight=1, uniform="a")
        self.rowconfigure(index=1, weight=1, uniform="a")
        self.rowconfigure(index=2, weight=1, uniform="a")
        self.rowconfigure(index=3, weight=1, uniform="a")
        self.rowconfigure(index=4, weight=1, uniform="a")

        menu_button1.grid(row=0, column=0, sticky="nswe", columnspan=2)
        menu_button2.grid(row=0, column=2, sticky="nswe")
        menu_button3.grid(row=1, column=0, columnspan=3, sticky="nsew")

        menu_slider1.grid(row=2, column=0, rowspan=2, sticky='nsew', pady=20)
        menu_slider2.grid(row=2, column=2, rowspan=2, sticky='nsew', pady=20)

        toggle_frame.grid(row=4, column=0, columnspan=3, sticky="nsew")
        menu_toggle1.pack(side="left", expand=True)
        menu_toggle2.pack(side="left", expand=True)

        entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor="center")


# Creating the Frame 2 (MAIN)
class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        self.create_widgets()

    def create_widgets(self):
        frame_1 = ttk.Frame(master=self)
        frame_2 = ttk.Frame(master=self)

        # FRAME 1
        box1 = ttk.Label(master=frame_1, text="Label1", background="blue", foreground="white")
        button1 = ttk.Button(master=frame_1, text="Button1")
        # FRAME 2
        box2 = ttk.Label(master=frame_2, text="Label2", background="red", foreground="white")
        button2 = ttk.Button(master=frame_2, text="Button2")

        frame_1.pack(side="left", expand=True, fill="both", pady=10, padx=10)
        frame_2.pack(side="left", expand=True, fill="both", pady=10, padx=10)

        box1.pack(expand=True, fill="both")
        button1.pack(expand=True, fill="both")

        box2.pack(expand=True, fill="both")
        button2.pack(expand=True, fill="both")

# Creating the instance of the object and run it
App("Class based app", (600, 600))
