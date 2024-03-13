from tkinter import *
import numpy as np
from scipy.io import wavfile
from pydub import AudioSegment
from os import listdir
import math


root = Tk()
song_dir = "songs"
attenuate_db = 0
accentuate_db = 2
var = DoubleVar()
rate = 1


def sel():
    global rate
    selection = "Value = " + str(var.get())
    label.config(text=selection)
    rate = int(var.get())


def bass_line_freq(track):
    global rate

    sample_track = list(track)

    est_mean = np.mean(sample_track)

    est_std = rate * np.std(sample_track) / (math.sqrt(2))

    bass_factor = int(round((est_std - est_mean) * 0.005))

    return bass_factor


def button_press():
    global song_dir
    for filename in listdir(song_dir):
        sample = AudioSegment.from_mp3(song_dir + "/" + filename)
        bassLineFreq = bass_line_freq(sample.get_array_of_samples())
        filtered = sample.low_pass_filter(bassLineFreq)

        combined = (sample - attenuate_db).overlay(filtered + accentuate_db)
        combined.export(
            "exports/" + filename.replace(".mp3", "") + "-export.mp3", format="mp3"
        )


sample1 = Scale(root, from_=10, to=20, length=600, orient=HORIZONTAL, variable=var)
sample1.pack()

button = Button(root, text="select", command=sel)
button.pack()


button2 = Button(root, text="create", command=button_press)
button2.pack()

label = Label(root)
label.pack()

root.mainloop()
