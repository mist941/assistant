import speech_recognition
import pyperclip
import time

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
microphone = speech_recognition.Microphone()

alias = "Емма"

def listen(recognizer, audio):
    try:
        query = recognizer.recognize_google(audio_data=audio, language = "uk-UA")
        print(query)
        if query.startswith(alias):
            pyperclip.copy(query.replace(alias, ""))
    except speech_recognition.UnknownValueError as err:
        print(err)

with microphone as source:
    sr.adjust_for_ambient_noise(source)

sr.listen_in_background(microphone, listen)
while True: time.sleep(0.1)