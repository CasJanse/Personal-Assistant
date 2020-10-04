import speech_recognition as sr
import pyaudio
from pynput import keyboard

recognizer = sr.Recognizer()


# region Convert microphone speech to text
def start_listening_to_voice():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Start recording")
        data = recognizer.listen(source)
        print("End recording")
        text = recognizer.recognize_google(data, language="en-US", show_all=True)
        print(text)
    # endregion


def on_press(key):
    try:
        print("alphanumerical key {0} pressed".format(key.char))
    except AttributeError:
        print("special key {0} pressed".format(key))
        if key == keyboard.Key.f11:
            print("Detected f11")
            start_listening_to_voice()


def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()




