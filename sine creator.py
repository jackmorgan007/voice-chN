import numpy as np
from scipy.io import wavfile


sample = int(input("rate ?"))
sampleRate = sample*100
frequency = int(input("frequency ?"))
length = 5

t = np.linspace(0, length, sampleRate * length)
y = np.sin(frequency * 2 * np.pi * t)

wavfile.write('Sine.wav', sampleRate, y)