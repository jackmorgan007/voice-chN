import PySimpleGUI as sg
while True:
    filename = sg.popup_get_file('Enter the file you wish to process')
    if filename[-3:] == "mp3":
        sg.popup('the file you entered is now being converted !')
        break
    else:    
        sg.popup('file is not valid !')
from os import path
from pydub import AudioSegment
input_file = filename
output_file = "result.wav"

sound = AudioSegment.from_mp3(input_file)
sound.export(output_file, format="wav")