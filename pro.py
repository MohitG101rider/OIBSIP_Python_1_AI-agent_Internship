import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
from gtts import gTTS
import pygame
import os
import random
import string
import time
import wikipedia
import pyjokes
import subprocess
import urllib.parse

'''#initialise
main=pyttsx3.init()'''

#hinglish speak
def speak_local(text):
    filename=''.join(random.choices(string.ascii_lowercase,k=8))+".mp3"
    tts=gTTS(text=text,lang='hi')
    tts.save(filename)

    pygame.init()
    pygame.mixer.init()
    pygame .mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.3)
    pygame.mixer.music.unload()
    os.remove(filename)

#functions
'''def speak(text):
    #convert text to speech
    main.say(text)
    main.runAndWait()'''

def take_command():
    try:
        #listen to you and convert your voice to text
        rec=sr.Recognizer()
        with sr.Microphone() as source:
            rec.adjust_for_ambient_noise(source,duration=0.5)
            print('just listening ...')
            audio=rec.listen(source,timeout=10,phrase_time_limit=10)
            
            print('Recognizing......')
            task=rec.recognize_google(audio, language='en-IN')
            return task.lower()

    except sr.WaitTimeoutError:
        print("Sleeping")
        return ""
    
    except sr.UnknownValueError:
        print('waiting')
        return ""
    except sr.RequestError:
        speak_local("Lagta hai net connect nahi hai.")
        return ""
    except Exception as e:
        print(" Error")
        speak_local("Unexpected Error , Try again")
    #return task.lower()

speak_local("Welcome Mohit , I am your assistant.")

while True:
    print("waiting for a call")
    c=take_command()
    print(c)

    if "theek hai" in c or "hello" in c:
        speak_local("Ha main sunn rahi hu, bolo")
        while True:
            c=take_command()
            if c.strip()=="":
                continue
            
            #features
            if "time" in c or "samay" in c or "tame" in c:
                current_time=datetime.datetime.now().strftime("%I:%M %p")
                speak_local(f" Time hai {current_time}")
            
            elif "wikipedia" in c :
                speak_local("wikipedia par kya search krna chahaoge ?")
                topic=take_command()
                if topic:
                    speak_local(f" Accha toh aap {topic} ke baare mein pata lagana chahate hai.")
                    try:
                        result=wikipedia.summary(topic, sentences=2)
                        print(" Summary : ",result)
                        speak_local(result)
                    except:
                        speak_local("WIKI se Koi data nahi mil paya, please repeat")
            elif "exit" in c or "bye" in c or "band kar" in c:
                speak_local("theek hai, bye, Have a Good Day")
                exit()
            elif "joke" in c or "jokes" in c or "chutkule" in c:
                joke=pyjokes.get_joke(language='en',category="neutral")
                speak_local("toh ye raha Joke aapki computer screen par")
                print(joke)
                speak_local(joke)
            elif "music" in c or "ganna" in c:
                file="E:\\USB Drive\\Received\\music"
                song_list=os.listdir(file)
                song=random.choice(song_list)
                path=os.path.join(file,song)
                speak_local(" Lo gaana suno aur chill kro")
                pygame.mixer.init()
                pygame.mixer.music.load(path)
                pygame.mixer.music.play()
                time.sleep(30)
                pygame.mixer.music.stop()
            elif "calculator" in c or "calculate" in c:
                speak_local(" Caclulation Time ")
                subprocess.Popen("calc.exe")
            elif "notepad" in c or "typing" in c or "type" in c:
                speak_local(" Typing Time ")
                subprocess.Popen("notepad.exe")
            elif "paint" in c or "ms piant" in c :
                speak_local(" Painting Time ")
                subprocess.Popen("mspaint.exe")
            elif "google" in c or "search" in c:
                speak_local(" Kya search krna hai ?")
                search=take_command()
                if search:
                    print(search)
                    speak_local(f" toh aap google par {search} search karna chahte ho !")
                    '''link_search=urllib.parse.quote_plus(search)
                    print(link_search)'''
                    url=f"https://www.google.com/search?q={search}"
                    print(url)
                    webbrowser.open(url)
                else:
                    speak_local(" Ek baar phir se bolo ")
            elif "so jao" in c or "aaram" in c:
                speak_local("theek hai , kuch kaam ho toh bolna")
                break
            else:
                speak_local("Kuch samajh nahi aaya , phir se bolo")
        





        


