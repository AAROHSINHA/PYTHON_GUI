import tkinter as tk
from tkinter import ttk

# Tkinter deos not have inbuilt tools for scrolling
# We can scroll on a canvas and add widgets on the canvas


class ListFrame(ttk.Frame):
    def __init__(self, parent, text_data, item_height):
        super().__init__(parent)
        self.pack(expand=True, fill="both")

        # widget data
        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height

        # canvas
        self.canvas = tk.Canvas(master=self, background="red", scrollregion=(0, 0, self.winfo_width(), self.list_height))
        self.canvas.pack(expand=True, fill="both")

        # display frame
        self.frame = ttk.Frame(master=self)

        for index, item in enumerate(self.text_data):
            self.create_item(index, item).pack(expand=True, fill="both", pady=4, padx=10)

        ttk.Label(master=self.frame, text="A LABEL").pack()
        self.canvas.create_window((0, 0),
                                  window=self.frame,
                                  anchor="nw",
                                  width=self.winfo_width(),  # entire window
                                  height=self.list_height)  # entire height
        # We have added the frame to canvas
        # Now we put the widgets in canvas

        # SCROLLING
        self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"))
        self.bind("<Configure>", self.update_size)

    def update_size(self, event):
        self.canvas.create_window((0, 0),
                                  window=self.frame,
                                  anchor="nw",
                                  width=self.winfo_width(),  # entire window
                                  height=self.list_height)

    def create_item(self, index, item):
        frame = ttk.Frame(self.frame)

        # grid layout
        frame.rowconfigure(index=0, weight=1)
        frame.columnconfigure(index=0, weight=1, uniform='a')
        frame.columnconfigure(index=1, weight=1, uniform='a')
        frame.columnconfigure(index=2, weight=1, uniform='a')
        frame.columnconfigure(index=3, weight=1, uniform='a')
        frame.columnconfigure(index=4, weight=1, uniform='a')

        # widgets
        ttk.Label(master=frame, text=f'#{index}').grid(row=0, column=0)
        ttk.Label(master=frame, text=f'{item[0]}').grid(row=0, column=1)
        ttk.Button(master=frame, text=f'{item[1]}').grid(row=0, column=2, columnspan=3, sticky='nsew')

        return frame
# setup
window = tk.Tk()
window.title("Scrolling")
window.geometry("500x400")

text_list = [('label', 'button'), ('hthing', 'click'), ('something', 'nothing'), ('another', 'hello'),
             ('goodbye', 'badbye'), ('label', 'button'), ('hthing', 'click'), ('something', 'nothing'),
             ('another', 'hello')]

list_frame = ListFrame(parent=window, text_data=text_list, item_height=100)

# Run window
window.mainloop()





