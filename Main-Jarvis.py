
'''conda install pyaudio
if any error occurs during pyudio installation 
install visual studio c++ and then try again installing pyaudio.'''

#pyttsx3 is a a text-to-speech conversion library in Python 

import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr  #pip install SpeechRecognition
import wikipedia  #pip install wikipedia
import webbrowser
import os
import smtplib
import random
import time
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    # It speaks a given string
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    # Wish according to the time.
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir, Your personal AI assistant , Please tell me how may I help you.")


def takeCommand():
    # It takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        clear()
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source) 
        # it converts the audio input into string

    try:
        clear()
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        # query = r.recognize_sphinx(audio)     #instead of that we can use this is offline but accuray very poor
        print(f"User said: {query}\n")
        time.sleep(2)
    except:
        clear()
        print("Say that again please....")
        time.sleep(1)
        return "None"
    return query


def sendEmail(to, content):
    # It sends an email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


def findReceiver(name):
    contacts = {"Name-A": "yourcontacts@gmail.com",
                "Name-b": "yourcontacts@gmail.com", "Name-c": "yourcontacts@gmail.com"}
    try:
        receiverGmail = contacts[name]
        return receiverGmail
    except:
        return 0


def givenews():
    apiKey = '49e391e7066c4158937096fb5e55fb5d'
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={apiKey}"
    r = requests.get(url)
    data = r.json()
    data = data["articles"]
    flag = True
    count = 0
    for items in data:
        count += 1
        if count > 10:
            break
        print(items["title"])
        to_speak = items["title"].split(" - ")[0]
        if flag:
            speak("Today's top ten Headline are : ")
            flag = False
        else:
            speak("Next news :")
        speak(to_speak)


def clear():
    # To clear the console after each command
    _ = os.system('cls')


if __name__ == '__main__':
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "how are you" in query:
            speak("I'm fine sir, how can i help you ?")
        elif "who are you" in query:
            speak("I'm jarvis desktop assistant made by Mr Sahil.")
        elif 'wikipedia' in query:
            # sentences=2 means return first two string
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open word' in query or 'open ms word' in query or 'ms word' in query:
            wordPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
            os.startfile(wordPath)
        elif 'open youtube' in query:
            webbrowser.open('http://www.youtube.com')
        elif 'open google' in query:
            webbrowser.open('https://www.google.co.in/')
        elif 'open stackoverflow' in query:
            webbrowser.open('https://stackoverflow.com/')
        elif 'play music' in query or 'play song' in query or 'play some music' in query or 'play another music' in query or 'change song' in query or 'next song' in query:
            music_dir = 'E:\\Media\\Musics\\Bollywood_songs'
            songs = os.listdir(music_dir)
            index=random.randint(0,1000)
            print(songs[index])
            os.startfile(os.path.join(music_dir, songs[index]))
            
        elif 'the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query or 'open visual studio' in query:
            codePath = "C:\\Users\\msahi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)
        elif 'email to' in query or 'send a mail' in query or 'mail to' in query:
            # This will send mail only if there is any matching name in last of query
            # like "email to sahil" or "mail to sahil" or "send a mail to my freind sahil"
            # notice last word in all strings contain a name which is exist as key in contacts (line 72)
            receiver = query.split(" ")[len(query.split(" "))-1]
            to = findReceiver(receiver)
            if to != 0:
                try:
                    speak("What is your message ?")
                    content = takeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    speak(
                        "Sorry bro, something went wrong and i am not able to send your email right now.")
        elif 'headlines' in query or 'news' in query or 'headline' in query:
            givenews()
        elif 'jarvis quit' in query or 'exit' in query or 'close' in query:
            speak("Thanks for using Jarvis!!!")
            exit()
        elif 'awesome' in query or 'wow' in query or 'amazing' in query or 'wonderful' in query:
            speak("Thank you sir, i am here for you")
        elif 'what' in query or 'who' in query or 'where' in query or 'can you' in query:
            webbrowser.open(f"https://www.google.com/search?&q={query}")
            speak(wikipedia.summary(query, sentences=2))
