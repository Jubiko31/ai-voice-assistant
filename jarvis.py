# Jarvis v0.1
import pyttsx3
import speech_recognition as sr
import subprocess
import webbrowser as wb
from time import sleep
from apps import CHROME

global engine

engine = pyttsx3.init('sapi5')
wb.register('chrome', None)

def speak(words):
    engine.say(words)
    engine.runAndWait()
    
def greet():
    speak("Welcome Back Boss")
    speak("How can I assist you today?")
    
def command():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source1:
            print("Waiting for command...")
            r.adjust_for_ambient_noise(source1, duration=0.2)
            r.pause_threshold = 1
            audio = r.listen(source1)
            words = r.recognize_google(audio)    
    except sr.RequestError as e:
        speak("Sorry boss, could not request results")
    except sr.UnknownValueError:
        speak("Sorry boss, could not process...")
    else:
        return words

def do(cmd):
    if "how are you" in cmd:
        speak("Trying to do better. What about you?")
        speak("by the way have you watched movie terminator?")
    elif "open chrome" in cmd:
        speak("yes sir")
        subprocess.call([CHROME, '--kiosk'])
    elif "open youtube" in cmd:
        speak("enjoy sir")
        wb.open("https://www.youtube.com")
    elif "sleep" in cmd:
        speak("Sure")
        sleep(60)
    elif "shutdown" in cmd:
        exit()
    else:
        greet()

greet()
while True:
    cmd = command()
    if cmd is not None:
        do(cmd.lower())