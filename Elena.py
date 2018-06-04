import pyttsx3
import speech_recognition as sr
import socket
import datetime
import json
import urllib.request

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #changing index changes voices but ony 0 and 1 are working here
engine.say('May i know your name')
engine.runAndWait()
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("May i know your name!")
    audio = r.listen(source)
try:
    print("you said\n:"+r.recognize_google(audio))
    message=r.recognize_google(audio)
    print(message)
except Exception as e:
    print(e)
name= message
response="hello "+message
engine.say(response)
engine.runAndWait()

def SayAgain():
    rep="Didn't get you can you repeat it again ?"
    engine.say(rep)
    engine.runAndWait()
    stt()
def developer():
    rep="My developer's name is ashirwad and his fellow collegues Rahul, priyanka and sachi"
    print(rep)
    engine.say(rep)
    engine.runAndWait()
    stt()
def elena(ques):
    if(ques=="what is your name"):
        MyName()
    elif(ques=="how are you"):
        HruReply()
    elif(ques=="I am fine" or ques=="all's well with me" or ques=="i am doing well" or ques=="I'm fine"):
        HruReply1()
    elif(ques=="who is your developer" or ques=="May i know who made you" or ques=="who are your developers" or ques=="who developed you"):
        developer()
    elif(ques=="exit" or ques=="bye" or ques=="talk to you later"):
        Exit()
    elif(ques=="who is the president of India"):
        presIndia()
    elif(ques=="which city is the capital of India" or ques=="Capital of India is" or ques=="what is the capital of india"):
        capIndia()
    elif(ques=="who is sofia "):
        whoSophia()
    elif(ques=="what do you think about sophia"):
        aboutSophia()
    elif(ques=="what is my IP " or ques=="what is my IP address"):
        ipAdd()
    elif(ques=="what is the weather forecast for today"):
        TodayWeather()
    else:
        print("no idea")
        SayAgain()
def TodayWeather():
    pass
    
def ipAdd():
    hostname=socket.gethostname()
    ipAddr=socket.gethostbyname(hostname)
    rep='your IP Address is '+ipAddr
    engine.say(rep)
    print(rep)
    engine.runAndWait()
    stt()

def whoSophia():
    rep="She is the first humonoid to be awarded citizenship "
    engine.say(rep)
    engine.runAndWait()
    stt()

def aboutSophia():
    rep="She is a amazing invention by the fellow humans"
    engine.say(rep)
    engine.runAndWait()
    stt()
    
def capIndia():
    rep="The captial of india is new delhi"
    engine.say(rep)
    print(rep)
    engine.runAndWait()
    stt()
def presIndia():
    rep="The name of honourable president of india is Ram Nath Kovind "
    engine.say(rep)
    print(rep)
    engine.runAndWait()
    stt()
def Exit():
    rep="byee have a good day "
    engine.say(rep)
    engine.runAndWait()
    quit()
def HruReply1():
    rep="Glad to hear that "
    engine.say(rep)
    print(rep)
    engine.runAndWait()
    rep1="what else ?"
    stt()
        
def HruReply():
    rep="I am fine "+name
    engine.say(rep)
    engine.runAndWait()
    rep1="what about you ?"
    engine.say(rep1)
    engine.runAndWait()
    print(rep)
    print(rep1)
    stt()
    
def MyName():
    engine.say("My name is elena")
    engine.runAndWait()
    print("My name is elena")
    stt()    

def tts(ques):
    ques=ques
    engine.say(ques)
    engine.runAndWait()
    elena(ques)
    
def stt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print(" ")
        audio = r.listen(source)
    try:
        print("\n"+r.recognize_google(audio))
        ques=r.recognize_google(audio)
        a="you said:-  "+ques
        print(a)
        tts(ques)
    except Exception as e:
        print(e)
stt()
#def sample():
#    engine.say(name)
#    engine.runAndWait()
#sample()
