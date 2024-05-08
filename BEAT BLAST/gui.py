
import pygame
import os
from pathlib import Path


from tkinter import *

pygame.init()
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\IA_2 BAP_PROJ\BEAT BLAST\assets\frame0")
SONGS_PATH = OUTPUT_PATH / "songs"
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


#function lists
def get_song_list():
    songs = []
    for file in os.listdir(SONGS_PATH):
        if file.endswith(".mp3"):
            songs.append(file)
    return songs

song_list = get_song_list()
current_song_index = 0


def previous_button_clicked():
    global current_song_index
    if current_song_index > 0:
        current_song_index -= 1
        print("Playing previous song:", song_list[current_song_index])
        play_button_clicked()
    else:
        print("Already at the first song.")



def next_button_clicked():
    global current_song_index
    if current_song_index < len(song_list) - 1:
        current_song_index += 1
        print("Playing next song:", song_list[current_song_index])
        play_button_clicked()
    else:
        print("Already at the last song.")


def play_audio(audio_path: str):
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

def pause_audio():
    pygame.mixer.music.pause()

def resume_audio():
    pygame.mixer.music.unpause()

def stop_audio():
    pygame.mixer.music.stop()

def play_button_clicked():
    global current_song_index
    audio_path = str(SONGS_PATH / song_list[current_song_index])
    print("Attempting to play audio:", song_list[current_song_index])
    play_audio(audio_path)
    print("Audio playback initiated.")
    
# Update the canvas to display the current song name
    canvas.itemconfig(up_song, text=song_list[current_song_index])


def pause_button_clicked():
    print("Pausing audio...")
    pause_audio()
    print("Audio paused.")

def resume_button_clicked():
    print("Resuming audio...")
    resume_audio()
    print("Audio resumed.")

def stop_button_clicked():
    print("Stopping audio...")
    stop_audio()
    print("Audio stopped.")



def display_song_list():
    song_names = "\n".join(song_list)
    canvas.itemconfig(song_text, text=song_names)

#layout
window = Tk()

window.geometry("589x376")
window.configure(bg = "#0E0B0B")


canvas = Canvas(
    window,
    bg = "#0E0B0B",
    height = 376,
    width = 589,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    294.0,
    32.0,
    image=image_image_1
)

canvas.create_text(
    82.0,
    19.0,
    anchor="nw",
    text="BEAT BLAST",
    fill="#FFFFFF",
    font=("Karmatic Arcade", 20 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    43.0,
    34.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    148.0,
    172.0,
    image=image_image_3
)

up_song=canvas.create_text(
    12.0,
    235.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("LEMON MILK", 20 * -1)
)

canvas.create_rectangle(
    301.0,
    73.0,
    580.0,
    270.0,
    fill="#FFFFFF",
    outline="")
#displaying songs list in the rectangle
song_text = canvas.create_text(
    301.0,
    73.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("LEMON MILK", 12)
)
display_song_list()
image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    294.0,
    322.0,
    image=image_image_4
)







#buttons
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=previous_button_clicked,
    relief="flat"
)
button_1.place(
    x=57.0,
    y=292.0,
    width=60.0,
    height=60.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=pause_button_clicked,
    relief="flat"
)
button_2.place(
     x=259.0,
    y=297.0,
    width=49.0,
    height=50.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=play_button_clicked,
    relief="flat"
)
button_3.place(
    x=130.0,
    y=297.0,
    width=42.0,
    height=50.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=stop_button_clicked,
    relief="flat"
)
button_4.place(
    x=314.0,
    y=297.0,
    width=48.0,
    height=50.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=next_button_clicked,
    relief="flat"
)
button_5.place(
    x=186.0,
    y=289.0,
    width=60.0,
    height=66.0
)
window.resizable(False, False)
window.mainloop()
