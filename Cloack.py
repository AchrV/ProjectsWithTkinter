from tkinter import *
from time import strftime
import datetime

root = Tk()
root.title("Tasos Test Clock with Day,Month, Date")
root.geometry("800x350")  #  window size that you can adjust to your liking

def update_time():
    string = strftime('%H:%M:%S %p')
    time_label.config(text=string)
    date_string = datetime.datetime.now().strftime("%A, %B %d, %Y")
    date_label.config(text=date_string)
    root.after(1000, update_time)

# The color scheme
background_color = "#282c34"  # A deep, calming blue-gray
text_color = "#abb2bf"       # Soft off-white

# Added a modern font and color scheme
time_label = Label(root, font=("Segoe UI Semibold", 80), background=background_color, foreground=text_color)
time_label.pack(expand=True, anchor='center')
time_label.config(borderwidth=8, relief="flat")

# Date label
date_label = Label(root, font=("Segoe UI", 30), background=background_color, foreground=text_color)
date_label.pack()

# Control frame for future expansion (like buttons)
control_frame = Frame(root, bg=background_color)
control_frame.pack(fill="x")

# Update time and date
update_time()

root.mainloop()

