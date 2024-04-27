import tkinter as tk
from tkinter import ttk


class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text):
        super().__init__(parent)

        # grid layout
        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1, uniform='a')
        self.columnconfigure(index=1, weight=1, uniform='a')
        self.columnconfigure(index=2, weight=1, uniform='a')

        ttk.Label(master=self, text=label_text).grid(row=0, column=0, sticky='nsew')
        ttk.Button(master=self, text=button_text).grid(row=0, column=1, sticky='nsew')

        self.pack(expand=True, fill='both', padx=10, pady=10)


# Create a Window
window = tk.Tk()
window.title("Widgets")
window.geometry('400x600')

# Widgets
Segment(window, 'label', 'button')  # Entire logic of this widget is in this segment
Segment(window, 'text', 'click')
Segment(window, 'hello', 'click')

Segment(window, 'label2', 'button2')  # Entire logic of this widget is in this segment
Segment(window, 'text2', 'click2')
Segment(window, 'hello2', 'click2')

# RUun the window
window.mainloop()
