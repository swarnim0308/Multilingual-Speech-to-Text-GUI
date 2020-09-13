from tkinter import *

##########################################################################
import speech_recognition as SRG
#Speech to Text conversion. Moreover, it supports various offline/online speech recognition engines and APIs.
import time
###########################################################################

root = Tk()
# Code to add widget will go here……..
root.geometry("600x500")
def sel():

    s=str(ivar.get())
    if s == '1':
        selection = "You selected the option English"
        label.config(text=selection)
        english()
    else:
        selection = "You selected the option Hindi"
        label.config(text=selection)
        hindi()

ivar = IntVar()
R1 = Radiobutton(root, text="English", variable=ivar, value=1,
                  command=sel,width=10,height=5)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Hindi", variable=ivar, value=2,
                  command=sel,width=10,height=5)
R2.pack( anchor = W )

def english():
    print("english")
    var = SRG.Recognizer()
    # to take the input in the audio format and recognize the sound
    with SRG.Microphone() as source:  # to fetch the audio from the microphone.
        audio_input = var.record(source, duration=8)
        print("Recording time:", time.strftime("%I:%M:%S"))
    try:
        text_output = var.recognize_google(audio_input)
    except:
        print("Couldn't process the audio input.")

    label1.config(text=":::::::::::::::::::Text converted from audio:::::::::::::::\n")
    label2.config(text=text_output)
    label.config(text="_____________________Thank You :)________________________")


    print(text_output)
    print("Execution time:", time.strftime("%I:%M:%S"))


def hindi():
    var = SRG.Recognizer()
    print("hindi")
    text = Text(root)
    with SRG.Microphone() as source:  # to fetch the audio from the microphone.
        audio_input = var.record(source, duration=10)
        print("Recording time:", time.strftime("%I:%M:%S"))
    try:
        text_output = var.recognize_google(audio_input, language='hi-IN')   # to take the input in the audio format and recognize the sound
    except:
        print("Couldn't process the audio input.")


    label1.config(text=":::::::::::::::::::Text converted from audio:::::::::::::::\n")
    label2.config(text=text_output)
    label.config(text="_____________________Thank You :)________________________")

    print(text_output)
    print("Execution time:", time.strftime("%I:%M:%S"))
label = Label(root)
label.pack()
label1 = Label(root)
label1.pack()
label2 = Label(root)
label2.pack()
w = Label(root, text="Choose language to Speak from Menu , Then Speak", width="90", height="45")
w.pack()

root.mainloop()

