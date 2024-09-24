# import tkinter library
from tkinter import *
# import extra special widgets like file opener
from tkinter import filedialog
#pygame for its audio capabilities
import pygame


# Creates instance of tkinter
root = Tk()

# To run in terminal, type python player.py or python3 player.py
root.title("MP3 Player")
root.geometry("700x400") # Makes the program however many pixels wide and tall

# Initialize Pygame and can start using it
pygame.mixer.init()


def add_song():
    # allows you to open finder and assigns the file to song
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files","*.mp3"),))
    # Strip out directory structure and mp3
    song = song.replace("/Users/ivanchen/Downloads/Computer Science/Python/mp3player/audio/", "")
    song = song.replace(".mp3", "")

    # initialdir allows you to choose the initial folder the program will open
    # my_label.config(text=song)
    # .config allows you to change the attribute of widgets
    playlist_box.insert(END, song)

# just put pass if you dont want the function to do anything yet
def add_many_songs():

    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    #loop through song list and replace directory
    for song in songs:
        song = song.replace("/Users/ivanchen/Downloads/Computer Science/Python/mp3player/audio/", "")
        song = song.replace(".mp3", "")

        playlist_box.insert(END, song)


# Create function to delete one song
def delete_song():
    #ANCHOR is the thing you highlight in the listbox
    playlist_box.delete(ANCHOR)

def delete_all_songs():
    # playlists are listed like a python list (starts from 0)
    playlist_box.delete(0, END)

def play():
    song = playlist_box.get(ACTIVE)
    # in order put the path back and .mp3 in order to play it
    song = f'/Users/ivanchen/Downloads/Computer Science/Python/mp3player/audio/{song}.mp3'

    # Load song with pygame mixer
    pygame.mixer.music.load(song)
    # Play song with pygame mixer
    pygame.mixer.music.play(loops=0)
    # loops determines how many times the song should be replayed

def stop():
    pygame.mixer.music.stop()

    # Unselect the song in playlist
    playlist_box.selection_clear(ACTIVE)

# Create Paused variable
global paused
paused = False
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        #unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        #pause
        pygame.mixer.music.pause()
        paused = True



# widget setup: widgetname = type(attributes)
# widgetname.pack() or widgetname.grid(row=, column=)
# Create playlist box
playlist_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="green", selectforeground='black')
playlist_box.pack(pady=20)

"""
# Define Button Images for controls
back_btn_img = PhotoImage(file='images/back.png')
forward_btn_img = PhotoImage(file='images/forward.png')
play_btn_img = PhotoImage(file='images/play.png')
pause_btn_img = PhotoImage(file='images/pause.png')
stop_btn_img = PhotoImage(file='images/stop.png')
Then to assign it to a button: back_button = Button(control_frame, image=back_btn_img, padx=10)
"""

# Create Button Frame
# Frames are like divs in html
control_frame = Frame(root)
control_frame.pack(pady=20)

# Create Play/Stop etc Buttons
back_button = Button(control_frame, text="Back", padx=10)
forward_button = Button(control_frame, text="Forward", padx=10)
play_button = Button(control_frame, text="Play", padx=10, command=play)
pause_button = Button(control_frame, text="Pause", padx=10, command=lambda: pause(paused)) # need to pass in whether the song is currently paused or not
stop_button = Button(control_frame, text="Stop", padx=10, command=stop)

back_button.grid(row=0, column=0)
forward_button.grid(row=0, column=1)
play_button.grid(row=0, column=2)
pause_button.grid(row=0, column=3)
stop_button.grid(row=0, column=4)

# Create Main Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Add Song Menu Dropdown
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song to Playlist", command=add_song)
add_song_menu.add_command(label="Add Many Songs to Playlist", command=add_many_songs)

# Create Delete Song Menu Dropdowns
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song From Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs From Playlist", command=delete_all_songs)

# temporary label
my_label = Label(root, text='')
my_label.pack(pady=20)



# keeps looping through to watch for changes such as mouse movement, button clicks
# calls and infinite loop that waits for events to happen on the client side and long as the window is not closed
root.mainloop()