import tkinter as tk
import speech_recognition as sr
import time

class SpeechToTextApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x500")
        self.language_var = tk.IntVar()
        self.label1 = None
        self.label2 = None
        self.label = None

        self.create_widgets()

    def create_widgets(self):
        # Label to display status or messages
        self.label = tk.Label(self.root, font=("Arial", 14, "bold"))
        self.label.pack()

        # Label to display text converted from audio
        self.label1 = tk.Label(self.root, font=("Arial", 12))
        self.label1.pack()

        # Label to display the converted text
        self.label2 = tk.Label(self.root, font=("Arial", 12), wraplength=500, justify=tk.LEFT)
        self.label2.pack()

        # Instruction label
        instruction_label = tk.Label(self.root, text="Choose a language and speak", font=("Arial", 14))
        instruction_label.pack(pady=20)

        # English language selection button
        english_btn = tk.Radiobutton(self.root, text="English", variable=self.language_var, value=1,
                                     command=self.recognize_speech, font=("Arial", 12))
        english_btn.pack(anchor=tk.W)

        # Hindi language selection button
        hindi_btn = tk.Radiobutton(self.root, text="Hindi", variable=self.language_var, value=2,
                                   command=self.recognize_speech, font=("Arial", 12))
        hindi_btn.pack(anchor=tk.W)

    def recognize_speech(self):
        # Determine the selected language based on the language_var value
        language = 'en-US' if self.language_var.get() == 1 else 'hi-IN'
        
        # Update label1 with a message
        self.label1.config(text=":::::::::::::::::::Text converted from audio:::::::::::::::\n")
        
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                # Record audio from the microphone for 8 seconds
                audio_input = recognizer.record(source, duration=8)
                print("Recording time:", time.strftime("%I:%M:%S"))
            
            # Use Google Speech Recognition to convert audio to text
            text_output = recognizer.recognize_google(audio_input, language=language)
            
            # Update label2 with the converted text
            self.label2.config(text=text_output)
            
        except sr.UnknownValueError:
            self.label2.config(text="Couldn't process the audio input.")
            
        except sr.RequestError:
            self.label2.config(text="Could not connect to the speech recognition service.")
        
        # Update the status label with a message
        self.label.config(text="_____________________Thank You :)________________________", font=("Arial", 14))

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeechToTextApp(root)
    root.mainloop()
