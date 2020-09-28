import speech_recognition as sr
import pyaudio

recognizer = sr.Recognizer()


# region Convert microphone speech to text
with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)
    print("Start recording")
    data = recognizer.listen(source)
    print("End recording")
    text = recognizer.recognize_google(data, language="en-US", show_all=True)
    print(text)
# endregion

