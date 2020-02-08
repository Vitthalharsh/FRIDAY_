#code made by vitthal
#your assistant FRIDAY
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia as wiki
import webbrowser as web
import os
import smtplib
engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
print(voice)
engine.setProperty('voices', voice[0].id)
print(voice[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takecommand():
    speak(f"yes sir what can i do for you ")
    a=(input("Ask any thing from me: "))
    return a
def sendemail(to,content):
    server=smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail","yourpass")#enter yours
    server.sendemail("your@gmail.com",to,content)
    server.close();
#-*-def takecommand():
    #it takes audio input from the user and
    #return a string
    #r=sr.Recognizer()
    #with sr.Microphone() as source :
    #    print("listining...")
    #    r.pause_threshold=1
    #    audio=r.listen(source)
    #try:
    #    print("recognizing")
    #    query=r.recognize_google(audio,language="en-in")
    #    print("user said"query)

    #except exception as :
    #    print("Say that again")
    #    return "none"
        #...
# -*- coding: utf-8 -*-

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning sir")
    elif hour>=12 and hour<15:
        speak("Good afternoon sir")
    else :
        speak("Good evening sir")

if __name__=="__main__":
    speak("Friday at your service sir")
    speak("HELLO HARSH")
    wishme()
    k=True
    cmd=input("DO YOU WNAT ME TO START: YES/NO: ").upper()
    if cmd =="YES":
      #  cmd=input("DO YOU WNAT ME TO START: YES/NO: ").upper()
        while cmd=="YES":

            query=takecommand()
            if 'wiki' in query:
                speak('searching wikipedia')
                query=query.replace('wiki',"")
                result=wiki.summary(query,sentences=2)
                speak("AS PER WIKIPEDIA")
                speak(result)
                web.open('wikipedia.com')
            elif 'youtube' in query:
                web.open('youtube.com')
            elif 'google' in query:
                web.open('google.com')
            elif 'cuims'in query:
                web.open('cuims.com')
            elif 'the time' in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(strTime)
          #  elif "No nothing"in query:
           #     k=False

            elif 'play movie' in query:
                speak(f"sir which movie")
                path="E:"
                os.startfile(path)
            elif 'email to' in query:
               try:
                   speak("Type the content of the email sir")
                   to="emailid@gmail.com"
                   content=input("ENTER YOUR TEXT HERE: ")
                   sendemail(to, content)
                   speak("Email sent!")
               except Exception as e:
                   print(e)
                   speak("SORRY SIR YOUR EMAIL HAS NOT BEEN SENT!!")
            speak("wanat to know more sir")
            cmd=input("Any thing more sir: ").upper()

if cmd=="NO":
    speak("ok sir bye bye ")




input("press enter")
