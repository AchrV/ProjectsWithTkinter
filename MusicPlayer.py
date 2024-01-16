import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

# Initialize music player GUI
music_player = tkr.Tk()
music_player.title("Test Music Player")
music_player.geometry("500x450")

# Function definitions for play, stop, pause, and unpause
def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

# Selecting music directory with error handling
directory = askdirectory()
if directory:
    os.chdir(directory)
    song_list = os.listdir()
else:
    print("No directory selected. Exiting...")
    music_player.destroy()

# Initialize pygame mixer
pygame.init()
pygame.mixer.init()

# Playlist setup using Comic Sans MS font
play_list = tkr.Listbox(music_player, font=("Comic Sans MS", 12), bg='white', fg='black', selectmode=tkr.SINGLE)
for item in song_list:
    play_list.insert('end', item)

# Creating buttons using  Comic Sans MS font
Button1 = tkr.Button(music_player, width=5, height=3, font=("Comic Sans MS", 12), text="PLAY", command=play, bg="green", fg="white")
Button2 = tkr.Button(music_player, width=5, height=3, font=("Comic Sans MS", 12), text="STOP", command=stop, bg="maroon", fg="white")
Button3 = tkr.Button(music_player, width=5, height=3, font=("Comic Sans MS", 12), text="PAUSE", command=pause, bg="navy", fg="white")
Button4 = tkr.Button(music_player, width=5, height=3, font=("Comic Sans MS", 12), text="UNPAUSE", command=unpause, bg="gold", fg="black")

# Song title label using  Comic Sans MS font
var = tkr.StringVar()
song_title = tkr.Label(music_player, font=("Comic Sans MS", 12), textvariable=var, background='white', foreground='black')

#  The Layout
song_title.pack(pady=10)
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
play_list.pack(fill="both", expand="yes")

# Mainloop
music_player.mainloop()