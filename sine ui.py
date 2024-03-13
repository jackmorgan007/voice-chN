from tkinter import *
import numpy as np
from scipy.io import wavfile

length = 5
inputrate = 0
root = Tk()
var = DoubleVar()
var2 = DoubleVar()
sampleRate = 0
frequency = 0


def sel():
    global sampleRate, inputrate
    selection = "Value = " + str(var.get())
    label.config(text=selection)
    inputrate = int(var.get())
    sampleRate = inputrate * 100


def sel2():
    global frequency
    selection = "Value = " + str(var2.get())
    label.config(text=selection)
    frequency = int(var2.get())


def sine():
    t = np.linspace(0, length, sampleRate * length)
    y = np.sin(frequency * 2 * np.pi * t)
    wavfile.write("Sine.wav", sampleRate, y)


sample1 = Scale(root, from_=0, to=10, length=600, orient=HORIZONTAL, variable=var)
frequency1 = Scale(
    root, from_=-100, to=100, length=600, orient=HORIZONTAL, variable=var2
)

sample1.pack()
button = Button(root, text="save", command=sel)
button.pack()
frequency1.pack()
button2 = Button(root, text="save", command=sel2)
button2.pack()
label = Label(root)
label.pack()
button3 = Button(root, text="create", command=sine)
button3.pack()

mainloop()
