
from tkinter import *  # Tkinter for GUI creation
from time import strftime  # strftime for time formatting
import datetime  # datetime module for date and time operations

# Creating the main window using Tkinter
root = Tk()
root.title("Tasos Test Clock with Day, Month, Date")  # Setting the window title
root.geometry("800x350")  # Setting the window size

# Function to update the time
def update_time():
    string = strftime('%H:%M:%S %p')  # Formatting the time
    time_label.config(text=string)  # Updating the time label
    date_string = datetime.datetime.now().strftime("%A, %B %d, %Y")  # Formatting the date
    date_label.config(text=date_string)  # Updating the date label
    root.after(1000, update_time)  # Scheduling the function to run every second

# Color scheme and font style configurations
background_color = "#282c34"  # A  gray color for the background
text_color = "#ffffff"  # White color for the text
font_style = "Arial 50"  # Font style for the clock display

# Creating and configuring the time label
time_label = Label(root, font=font_style, bg=background_color, fg=text_color)
time_label.pack(anchor='center')  # Placing the label in the center of the window

# Creating and configuring the date label
date_label = Label(root, font=("Arial", 20), bg=background_color, fg=text_color)
date_label.pack(anchor='s')  # Placing the label at the bottom of the window

# Initializing the time update process
update_time()

# Running the application
root.mainloop()

