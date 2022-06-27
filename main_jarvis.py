from cgitb import text
from tkinter import Variable
import pyttsx3
import speech_recognition as sr
import datetime
import os
import psutil
import speedtest
import cv2
import operator
from requests import get
from bs4 import BeautifulSoup
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import MyAlarm
import keyboard
import sys
import numpy
import os.path
import smtplib
from PIL import Image
from pywikihow import search_wikihow,WikiHow
import time
import pyjokes
from pyautogui import *
import requests
import pyautogui
import pywhatkit as kit
import os.path
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
# print(voices[0].id)
engine.setProperty('voices', voices[len(voices) - 1].id)
#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
#To convert voice into text
def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        
        return "none"
    return query
#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("i am jarvis sir. please tell me how may i help you")
#for news updates
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=GET YOUR API FRON NEWS API WEBSITE'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page['articles']
    # print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")
#for taking screenshot
def screenshot():
            pyautogui.screenshot(f"C://SCREEN SHOT FOLDER PATH WITH DOUBLE '/'//screenshot.png")
#main program
def TaskExicution():    
    wish()
    while True:
        query = takecommand().lower()
#TO OPEN NOTEPAD      
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
#SELF         
        elif 'hi' in query or 'hello' in query:
            speak('Hello sir, how may I help you?')
       
        elif 'power' in query:
            speak("i am very high tec ai made by kunal singh ,on 25th may 2022, i can do many things online aswell as ofline")
       
        elif 'who are you'in query:
            speak("i am advance jarvis,which can do many things and i am made in python language")
       
        elif 'who is kunal'in query or 'kon hai kunal' in query:
            speak(" kunal singh is my mast who made me ")    
#TO OPEN ADOBE READER        
        elif "open adobe reader" in query:
            apath = "C:\\PATH OF THE ACROBAT.EXE FILE WITH DOUBLE'\'\\AcroRd32.exe"
            os.startfile(apath)
#TO OPEN CMD
        elif "open command prompt" in query or "open cmd" in query:
            os.system("start cmd")
#TO OPEN CAMERA
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
#TO PLAY MUSIC
        elif "play music" in query:
            music_dir = "E:\\KUNAL\\music"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))
# FOR GETTING IP ADDRESS
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
# FOR SEARCHING ANY THING ON WIKIPEDIA WORK IN TERMINAL
        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
# TO KNOW WHERE ARE YOU LIKE WHICH CITY, STATE, COUNTRY        
        elif 'where i am' in query:
            speak("wait sir , letme connect to the internet")
            try:
                ADD = requests.get('https://api.ipify.org').text
                print(ADD)
                URL = 'https://get.geojs.io/v1/ip/geo/'+ADD+'.json'
                geo_rs = requests.get(URL)
                geo_data = geo_rs.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"sir i am not shure,but i think we are in {city} city of {country} country")
            except:
                speak("sorry sir i am not able to find were we are because of network issue")
                pass    
#TO KNOW INTERNET SPEED\
        elif "what is internet speed" in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")
            print(dl)
            print(up)
            try:
                os.system('cmd /k "speedtest"')
            except:
                speak("there is no internet connection") 
# TO KNOW HOW MUCH POWER LEFT IN ADVANCE METHOD
        elif "how much power left" in query or "how much power we have " in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Sir our system have {percentage}percent battery")
            if percentage >= 75:
                speak("we have enough power to continue our system")
            elif 40 <= percentage <= 75:
                speak("we should connect our system to charging point to charge our battery")
            elif 15 <= percentage <= 30:
                speak("we don't have enough power to work,please connect to charging")
            elif percentage <= 15:
                speak("we have very low power , please connect to charging the system will shutdown very soon")
# TO HIDE FILE
        elif "hide all files" in query:
            os.system("attrib +h /s /d")
            speak("sir all files in this folder are hidden ")
# TO VISIBLE THE FILE WHICH IS HIDDEN
        elif "visible for everyone" in query:
            os.system("attrib -h /s /d")
            speak("sir all files in this folder are visible to everyone ")
# TO TAKE SCREENSHOT
        elif"screenshot" in query:
            screenshot()
            speak("i am done sir, the screenshot is saved in our main folder, now i am ready for command")
# FOR DOING CALCULATION WITH AUDIO ONLY
        elif "do some calculation" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("say what you want to calculate")
                print("listening......")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                my_stringer = r.ecognizer_google(audio)
                print(my_stringer)
            def get_operator_fn(op):
                return {
                    "+": operator.add,
                    "-": operator.sub,
                        
                    "*": operator.mul,
                    "divided": operator.__truediv__,
                }[op]

            def eval_binary_expr(op1, oper, op2):
                op1, op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)

                speak("your result is")
                speak(eval_binary_expr(*(my_stringer.split())))
# FOR GETTING TEMPERATURE
        elif "temperature" in query:
            speak("for which place you want to know the temparature")
            search = takecommand()# PLACE NAME
            url = (f"https://www.google.com/search?q=temparature+in+{search}")
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text      
            speak(f" current temparature of{search} is {temp}")
            print(f"current temperature of {search} is {temp}")
# TO INCREASE VOLUME
        elif "volume up" in query:
            pyautogui.press("volumeup")
# TO DECREASE VOLUME       
        elif "volume down" in query:
            pyautogui.press("volumedown")
# TO MUTE VOLUME       
        elif "mute" in query:
            pyautogui.press("volumemute")
# TO SEARCH LIKE HOW TO COOK CAKE...
        elif "activate how to mode" in query:
            speak("How to mode is Activated please tell me what you want to know ")
            while True:
                how = takecommand()
                try:
                    if "exit" in how:
                        speak("okay sir how to mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) - -1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except:
                    speak("sorry sir i am not able to find this")
# TO SEARCH LIKE WHAT IS CAPITAL OF INDIA
        elif "activate what is to mode" in query:
            speak("What is mode is Activated please tell me what you want to know ")
            while True:
                what = takecommand()

                try:
                    if "exit" in what:
                        speak("okay sir,what is mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how_to, max_results)
                        assert len(how_to) - -1
                        how_to[0].print()
                        speak(how_to[0].summary)

                except:
                    speak("sorry sir i am not able to find this")
# TO SEARCH LIKE WHAT DO YOU MEAN BY CONCAVE LENS
        elif "activate what do you mean mode" in query:

            speak("what do you mean by mode is Activated please tell me what you want to know ")
            while True:
                what_do = takecommand()
                try:
                    if "close" in what_do:
                        speak("okay sir what do you mean by mode is close ")
                        break
                    else:
                        max_results = 1
                        what_do_you_mean_by = search_wikihow(what_do, max_results)
                        assert len(what_do_you_mean_by) - -1
                        what_do_you_mean_by[0].print()
                        speak(what_do_you_mean_by[0].summary)
                except:
                    speak("sorry sir, i am not able to find this")
# TO SET ALARM
        elif "alarm" in query:
            speak("sir please tell me the time to set alarm,for example set alarm to 5:30 am")
            pp = takecommand()
            pp = pp.replace("set alarm to", "")
            pp = pp.replace(".", "")
            pp = pp.upper()
            MyAlarm.alarm(pp)
# TO OPEN YOUTUBE
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
# TO SEARCH ANYTHING ON GOOGLE BY VOICE
        elif 'google' in query:
                query = query.replace("google", "")
                query = query.replace("it", "")
                speak('here you go ')
                url69 = 'https://google.com/search?q=' + query
                webbrowser.open(url69)   
# TO OPEN ANY WEBSITE
        elif  "open website" in query:
                speak("Tell me the name of the website")
                search = takecommand()
                speak('Opening' + search)
                url = 'www.' + search +'.com'
                webbrowser.open(url) 
# TO SEND WHATSAPP MESSAGE BY COMMAND
#  IF IT WILL NOT WORK THEN PLS TELL ME BY COMMENTING
        elif "send whatsapp message" in query:
            speak("to whome you want tosend message")
            tyty = f"type the number here :{input()}"
            speak("waht you have to send in the massage?")
            ytyt = input()
            kit.sendwhatmsg(f"+91{tyty}", "{ytyt}",4,13)
            time.sleep(50)
            speak("message has been sent")
# TO PALY YOUTUBE SONG
        elif "song on youtube" in query:
            kit.playonyt("excuses")
# TO SET TIMER            
        elif 'timer' in query or 'stopwatch' in query:
            speak("For how many minutes?")
            timing = takecommand()
            timing =timing.replace('minutes', '')
            timing = timing.replace('minute', '')
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing * 60
            speak(f'I will remind you in {timing} seconds')

            time.sleep(timing)
            speak('Your time has been finished sir')
# TO CLOSE THE COMPUTER PROGRAM    
        elif "thankyou" in query:
            speak("thanks for using me sir, have a good day.")
            break;
# FOR HEARING JOKE            
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
# TO SHUTDOWN THE SYSTEM
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")
# TO RESTART THE SYSTEM
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
# TO SLEEP THE SYSTEM
        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
# TO SWITCH WINDOW
        elif "change window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(2)
            pyautogui.keyUp("alt")

# TO HEAR DAILY HEADLINES                   
        elif "news" in query:
            speak("please wait sir, feteching the latest news")
            news()
# RUN PROGRAM
if __name__ == "__main__":
    while True:
        fury = takecommand()
        if 'wake up' in fury or 'are you there' in fury:
            speak("welcome back sir\mam")
            TaskExicution()
            
        elif 'goodbye' in fury or 'bye jarvis' in fury:
            sys.exit()
                