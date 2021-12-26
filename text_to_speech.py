import requests
import pyttsx3
import random
import string

def text_to_speech(word):
    url = f"https://internal.nutq.uz/api/v1/cabinet/synthesize/?format=api&t={word}"
    rep = requests.get(url)
    with open('movie.wav', 'wb') as f:
        f.write(rep.content)
    return rep
def text_to_speech2(word):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', "english-us")
    engine.setProperty('rate',140)
    engine.save_to_file(word, 'movie.wav')
    engine.runAndWait()