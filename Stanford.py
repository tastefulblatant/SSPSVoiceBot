import speech_recognition as sp
import pyttsx3
import pywhatkit
import pyautogui
from colorama import Fore
import random
import datetime
import os
import time


greet =  ['hi', 'hello', 'hey', 'hi how are you', 'whats up', 'hey there', 'hello there', 'hello there', 'hi there']
fgreet = random.choice(greet)

r = sp.Recognizer()

def clear():
    os.system('cls')
    print(f"""          
  ██████ ▄▄▄█████▓ ▄▄▄       ███▄    █   █████▒▒█████   ██▀███  ▓█████▄ 
▒██    ▒ ▓  ██▒ ▓▒▒████▄     ██ ▀█   █ ▓██   ▒▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌
░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▓██  ▀█ ██▒▒████ ░▒██░  ██▒▓██ ░▄█ ▒░██   █▌
  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░▒██▀▀█▄  ░▓█▄   ▌
▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒▒██░   ▓██░░▒█░   ░ ████▓▒░░██▓ ▒██▒░▒████▓ 
▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ 
░ ░▒  ░ ░    ░      ▒   ▒▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒ 
░  ░  ░    ░        ░   ▒      ░   ░ ░  ░ ░   ░ ░ ░ ▒    ░░   ░  ░ ░  ░ 
      ░                 ░  ░         ░            ░ ░     ░        ░    
                                                                 ░      
            By TASTEFULBLATANT#3056 & Oliverrr#8393
            Say "help" for commands
            """)
    

def speak(command):
    voice = pyttsx3.init()
    voice.say(command)
    voice.runAndWait()


def commands():
    try:
        with sp.Microphone() as source:
            
            clear()
            speak(f"{fgreet}, what can i do for you?")
            time.sleep(2)
            while True:
                print("Say command..")

                r.adjust_for_ambient_noise(source)
                audion = r.listen(source)
                my_text = r.recognize_google(audion)
                my_text = my_text.lower() 

                

                if "help" in my_text:
                    speak("I will create and open .txt file.")
                    clear()
                    with open("commnad.txt","w") as file:
                        print(file.write(""" 
Help: Say Help and StanFord will create this file :)
Time: Say Time and StanFord will tell you, what time is right now.
Date: Say Date and StaFord will tell you, what date is right now.
Play: Say Play + name of the video what you want and StanFord will play you the video.
About: Say About and StanFord will tell you something about me.
Search: Say Search and StanFord will search you what you want.
Volume: Say volume up, volume down or volume mute, StanFord will do it for you.
                        """))
                        print("")
                        clear()
                        


                elif "play" in my_text:
                    my_text = my_text.replace("play", "")
                    speak("Have a nice video!")
                    speak(f'playing {my_text}')
                    pywhatkit.playonyt(my_text)
                    clear()

                elif "time" in my_text: 
                    os.system('cls')
                    TimeNow = datetime.datetime.now().strftime('%H:%M')
                    clear()
                    print(TimeNow)
                    speak(TimeNow)
                    clear()

                elif "about ssps" in my_text:
                    clear()
                    print("SSPŠ is high school located in Smíchov, Prague. It was founded in 1901 and now has over 600 students in 20 classes. Currently, classes in the fields of Information Technology, Cybersecurity and Gymnasium are taking place here.") 
                    speak("SSPŠ is high school located in Smíchov, Prague. It was founded in 1901 and now has over 600 students in 20 classes. Currently, classes in the fields of Information Technology, Cybersecurity and Gymnasium are taking place here.")
                    clear()


                elif "date" in my_text:
                    date = datetime.date.today()
                    clear()
                    print(date)
                    speak(date)
                    clear()

                elif "search" in my_text:
                    clear()
                    my_text = my_text.replace("search", '')
                    pywhatkit.search(my_text)
                    clear()  

                elif "volume up" in my_text:
                    pyautogui.press("volumeup")
                
                elif "volume down" in my_text:
                    pyautogui.press("volumedown")
                    
                elif "mute volume" in my_text:
                    pyautogui.press("volumemute")
                
                elif "exit" in my_text:
                    clear()
                    speak("Good bye, have a nice day sir.")
                    exit()
                    

                elif '' in my_text:
                    speak("Say something")


    except:
        print("Error, install module: pip install PyAudio")

commands()
