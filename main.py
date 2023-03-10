
from email import message
import sys
import time
import os
import webbrowser
#Importing Speach Recognition
import speech_recognition as sr
import os
import pyttsx3



engine = pyttsx3.init()
engine.say("Listening")
engine.runAndWait()
os.system('cls') # clear console output for better user expericence

#-- Error Messages --
r = sr.Recognizer()
message_00 = "Listening..."
message_01 = "Processing..."
print(message_00)


def listening():
    with sr.Microphone() as source:
        audio = r.listen(source) # Listening
    
        for char in message_01: # Processing
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        print("")
        try:
            user_command = r.recognize_google(audio)
        except:
            user_command = ""
        user_command = user_command.lower()
        print(user_command)

    return user_command

user_command = listening()

def check_terms(terms): # checking for keyword if true then we can execute some function like searcing internet.
    for term in terms:
        if term in user_command:
            print(term)
            return True

if user_command == "":
    user_command = listening()

if user_command == "hello" or user_command == "hey" or user_command == "hi" or user_command == "tommy" or user_command == "hey tommy" or user_command == "hello tommy" or user_command == "hi tommy": # basic frist intraction.
    engine.say(" Hi, May I know who is this?")
    engine.runAndWait()
    print(message_00)
    with sr.Microphone() as source:
        audio = r.listen(source) # Listening
    
        for char in message_01: # Processing
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        print("")
    
        user_command = r.recognize_google(audio)
        user_command = user_command.lower()
        print(user_command)
    user = user_command.split(" ")[-1]
    user = "Hi , " + user + " "
    engine.say(user)
    engine.runAndWait()
    engine.say("Nice to mee you!")
    engine.runAndWait()

va_name = "Tommy" # default VA name

if user_command == "who is this": # asksing who are you talking to
    engine.say("I am your Virtual Assistant," + va_name)
    engine.runAndWait()


if user_command == "where are you from": # where are you from
    engine.say("I am from world of computer")
    engine.runAndWait()


if user_command == "who is your creator": # who is your creator
    engine.say("My creator is Zodiac")
    engine.runAndWait()


if check_terms(['shutdown','tommy off']): # Shutdown V_A
    engine.say("shutting down, sir")
    engine.runAndWait()

if check_terms(["your name should be"]):
    engine.say("My name is now," + va_name)
    engine.runAndWait()

    engine.say("Thank you, sir,")
    engine.runAndWait()
    user = user_command.split("be")[-1]
    va_name = user

if check_terms(['search for','google']) and ["youtube","search youtube for","search on youtube"] not in user_command:
    search_term = user_command.split("for")[-1]
    url = "http://www.google.com/search?" + search_term
    webbrowser.ger().open(url)
    engine.say("Searching"+ search_term + "on google")
    engine.runAndWait()

if check_terms(["search youtube for","search on youtube"]):
    if "search" and "on youtube" in user_command:
        search_term = user_command.split("search")[1][-2] # search[0] "XYZ" on[-2] youtube[-1]
        url = "http://www.youtube.com/results?search_query=" + search_term
        webbrowser.ger().open(url)
        engine.say("Searching"+ search_term + "on youtube")
        engine.runAndWait()

    if "search youtube for" in user_command:
        search_term = user_command.split("for")[-1]
        url = "http://www.youtube.com/results?search_query=" + search_term
        webbrowser.ger().open(url)
        engine.say("Searching"+ search_term + "on youtube")
        engine.runAndWait()

