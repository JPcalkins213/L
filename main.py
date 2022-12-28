from datetime import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import wolframalpha

engine = pyttsx3.init()
r = sr.Recognizer()
m = sr.Microphone()

print("Listening")
with m as source:
    r.adjust_for_ambient_noise(source)

def say(sentence):
    engine.say(sentence)
    engine.runAndWait()

def listen():
    print("say something")
    with m as souce:
        audio = r.listen(source)
    print("got it")
    try:
        phrase = r.recognize_google(audio, show_all=False, language='en_US')
        confirmation = 'Got it, you said ' + phrase
        engine.say(confirmation)
        engine.runAndWait()
    except:
        print("sorry didnt catch that")
        engine.say("sorry didnt catch that")
        engine.runAndWait()
    return phrase
