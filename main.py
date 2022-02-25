from email import message
from urllib import request
import pyttsx3
import pyaudio
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import openingText
import requests
from tasks.offline_tasks import open_camera, open_calculator, open_cmdprompt, open_notepad
from tasks.online_tasks import find_my_ip, search_on_google, search_on_wikipedia, send_wts_msg, play_on_yt, get_random_advice, get_random_joke, get_top_IMDB_movies, get_latest_news, get_weather_news

#------------Declaring the user and botname----------
USERNAME= "Sugam Chand M" 
BOTNAME= "Ren"

# ---------Setting up a Speak Engine-------------------
engine=pyttsx3.init('sapi5')
engine.setProperty('rate', 190) #set rate
engine.setProperty('volume', 1.0)  #set volume
voices=engine.getProperty('voices') 
engine.setProperty('voice',voices[0].id)  #set voice [Here I have set a male voice. If you want a female voice set voices[1].id]

# ---------Setting up the Speak function----------------
def speak(text):      #The function enables the assistant to speak/say whatever the text is passed to it
    engine.say(text)
    engine.runAndWait()

# ---------Setting up the greet function----------------
def greet():     # Greets the user according to the time
    hour=datetime.now().hour
    if (hour>=6) and (hour<12):
        speak(f"Good Morning my Master {USERNAME}")
    elif (hour>=12) and (hour<16):
        speak(f"Good Afternoon my Master {USERNAME}")
    elif (hour>=16) and (hour<19):
        speak(f"Good Evening my Master {USERNAME}")
    speak(f"Hi I am {BOTNAME}, your personal assistant. How may I help you?")

# ---------Setting up the user_input function to take the user input--------------
def user_input():  #takes input from the user, recognizes it using the speech_recognition module and converts it into text
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening my master......")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing my master......")
        query=r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(openingText))
        else:
            hour=datetime.now().hour
            if(hour>=21) and (hour<6):
                speak(f"Good night my Master, take care!")
            else:
                speak(f"Have a good day Master")
            exit()
    except Exception:
        speak(f"Sorry master, I could not understand. Could you please repeat that again?")
        query='None'
    return query

#---------------Main Function-------------------
if __name__=='__main__':
    greet()
    while True:
        query=user_input().lower()

        if 'who are you' in query:
            speak(f"Hello I am REN version 1 point O, a virtual assistant created by my master {USERNAME}")

        elif 'notepad' in query:
            open_notepad()

        elif 'calculator' in query:
            open_calculator()

        elif 'camera' in query:
            open_camera()
        
        elif 'command prompt' in query:
            open_cmdprompt()

        elif 'ip address' in query:
            ip_addr=find_my_ip()
            speak(ip_addr)
            speak(f"For your convinience I'm printing it on the screen, master")
            print(f"Your IP address is:- {ip_addr}")

        elif 'youtube' in query:
            speak(f"What video you want play on Youtube, master?")
            video=user_input().lower()
            play_on_yt(video)

        elif 'search on google' in query:
            speak(f"What do you want to search on google, master?")
            query=user_input().lower()
            search_on_google(query)

        elif 'wikipedia' in query:
            speak(f"What do you want to search on wikipedia, master")
            query=user_input().lower()
            results=search_on_wikipedia(query)
            speak(f"According to Wikipedia, {results}")
            speak(f"For your convinience I'm printing it on the screen, master")
            print(results)

        elif 'send whatsapp message' in query:
            speak(f"To what number should I send the message, master? Please enter in the console")
            number=input("Enter the number:- ")
            message=user_input().lower()
            send_wts_msg(number,message)
            speak(f"I have sent the message, master")
        
        elif 'joke' in query:
            speak(f"Hope you like this one, master")
            joke=get_random_joke()
            for i in range(0,1):
                speak(joke[i])
                speak(f"For your convinience I'm printing it on the screen, master")
                print(joke[i])

        elif 'advice' in query:
            speak(f"Here's an advice for you, master")
            advice=get_random_advice()
            speak(advice)
            speak(f"For your convinience I'm printing it on the screen, master")
            print(advice)

        elif 'top imdb movies' in query:
            speak(f"I'm printing the top 10 of top 250 IMDB movies in the terminal, master")
            list=get_top_IMDB_movies()
            for i in range(0,10):
                speak(list[i])
                print(list[i])

        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, master")
            speak(get_latest_news())
            speak(f"For your convinience I'm printing it on the screen, master")
            print(*get_latest_news(),sep='\n')
        
        elif 'weather' in query:
            #ip_addr=find_my_ip()
            city='Bangalore'     #requests.get(f"https://ipapi.co/{ip_addr}/city/").text
            speak(f"Getting the weather report of your city {city}, master")
            weather,temp,feels_like=get_weather_news(city)
            speak(f"The current temperature is {temp}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temp}\nFeels like: {feels_like}")
    
