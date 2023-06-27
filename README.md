# Speech to Text App

This is a simple Python application that utilizes the `tkinter` and `speech_recognition` libraries to convert speech into text. The application provides a graphical user interface (GUI) where the user can choose a language and speak into a microphone for the audio to be recognized and converted to text.

## Prerequisites

- Python 3.x installed on your system.
- The following Python libraries need to be installed:
  - `tkinter` for creating the GUI.
  - `speech_recognition` for performing speech recognition.

## Installation

1. Clone or download the code from the repository.
2. Make sure you have the required libraries installed by running the following command in your terminal or command prompt:

pip install tkinter speech_recognition


## Usage

1. Open a terminal or command prompt and navigate to the directory where the code is located.
2. Run the following command to start the application:

python speechRecognitionGUI.py


Replace `<filename>` with the name of the Python file that contains the code.
3. The application window will open, displaying two labels and language selection buttons.
4. Choose the desired language (English or Hindi) by selecting the corresponding radio button.
5. Click on the "Choose a language and speak" label and speak into the microphone.
6. After speaking, the application will process the audio and display the converted text in the GUI.

## Functionality

- The application uses the `tkinter` library to create the GUI with labels and radio buttons for language selection.
- The `recognize_speech` method is called when a language selection button is clicked.
- The selected language is passed to the Google Speech Recognition service to convert the audio input to text.
- The converted text is displayed in the GUI.
- Error handling is implemented to handle situations where audio processing or speech recognition fails.
- The application continues to run until the user closes the window.

## Notes

- Make sure you have a working microphone connected to your system for audio input.
- The application records audio for 8 seconds, you can adjust the duration as per your requirements.
- The `language` variable can be modified to support additional languages if desired. Currently, English (en-US) and Hindi (hi-IN) are supported.
- The application prints the recording time to the console for reference.

## Acknowledgements

- This code utilizes the `speech_recognition` library for speech recognition functionality.
- The GUI is created using the `tkinter` library.

## License

[MIT License](https://opensource.org/licenses/MIT)
