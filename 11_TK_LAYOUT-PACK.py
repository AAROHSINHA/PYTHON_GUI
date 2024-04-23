import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('PACK')
window.geometry('400x600')

# Top Frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(master=top_frame, text="Label1", background="red", foreground="white")
label2 = ttk.Label(master=top_frame, text="Label2", background="blue", foreground="white")

# Middle Widget
label3 = ttk.Label(window, text="Another Label", background="green", foreground="white")

# Bottom Frame
bottom_frame = ttk.Frame(window)
label4 = ttk.Label(master=bottom_frame, text="Last Of The Labels", background="orange", foreground="white")
button = ttk.Button(master=bottom_frame, text="A Button")
button2 = ttk.Button(master=bottom_frame, text="Another Button")

# BUTTON FRAME
button_frame = ttk.Frame(bottom_frame)
button_bottom1 = ttk.Button(master=button_frame, text="BUTTONNN")
button_bottom2 = ttk.Button(master=button_frame, text="BUTTONNN")
button_bottom3 = ttk.Button(master=button_frame, text="BUTTONNN")

# TOP LAYOUT
label1.pack(side="left", fill="both", expand=True)
label2.pack(side="left", fill="both", expand=True)
top_frame.pack(fill="both", expand=True)

# MIDDLE LAYOUT
label3.pack(expand=True)

# BOTTOM LAYOUT
button.pack(side="left", expand=True, fill="both")
label4.pack(side="left", expand=True, fill="both")
button2.pack(side="left", expand=True, fill="both")
bottom_frame.pack(expand=True, fill="both", padx=20, pady=20)

# BUTTON FRAME
button_bottom1.pack(side="top", expand=True, fill="both")
button_bottom2.pack(side="top", expand=True, fill="both")
button_bottom3.pack(side="top", expand=True, fill="both")
button_frame.pack(expand=True, fill="both", padx=10, pady=10)

# Run the window
window.mainloop()
