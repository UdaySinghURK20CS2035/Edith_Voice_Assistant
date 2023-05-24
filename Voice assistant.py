import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit as kit
import pyautogui
from selenium import webdriver
import time
import random
import pyjokes



engine=pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again Please....")
        return "None"
    return query

def wishme():

    while True:
        speak('Whom am I speaking too')
        query= takecommand().lower()
        query = query.split(' ')
        name = query[-1]
        if name != None:
            break

    d = f'{name} I am always here to help you',f'tell me how can I help you {name}', f'What can I do for you {name}'
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning {name}!")
    elif(hour>=12 and hour<18):
        speak(f"Good Afternoon {name}!")
    else:
        speak(f"Good Evening {name}!")
    speak("Sir I am edith.")
    speak(random.choice(d))

if __name__ == '__main__':
    wishme()
    while True:
        query= takecommand().lower()
        if 'edit' in query:
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif 'youtube' in query and 'close youtube' not in query:
                speak(f"{name} what should I play")
                cmd = takecommand().lower()
                kit.playonyt(f"{cmd}")
                continue

            elif 'close youtube' in query:
                pyautogui.moveTo(pyautogui.size().width - 1, 1)
                time.sleep(0.5)
                # click the close button
                pyautogui.click()

            elif 'gmail' in query:
                webbrowser.open("mail.google.com")

            elif 'close gmail' in query:
                webbrowser.close()

            elif 'time' in query:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"{name} the time is {strtime}")

            elif 'code' in query:
                codepath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)

            elif 'google' in query:
                speak(f"{name} what should I search")
                search = takecommand().lower()
                webbrowser.open(f'{search}')

            elif 'karunya online' in query:
                webbrowser.open("https://online.karunya.edu/students/home")

            elif 'switch the tab' in query:
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.keyUp('alt')

            elif 'sleep' in query:
                speak(f"Thankyou {name} for using me as your assistant")

            elif 'tell me a joke' in query:
                My_joke = pyjokes.get_joke(language="en", category="all")
                speak(My_joke)

            elif 'terminate' in query:
                speak(f"Terminating myself {name}")
                break

