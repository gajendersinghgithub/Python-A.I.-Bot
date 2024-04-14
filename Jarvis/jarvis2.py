import pyttsx3                      # Python library that will help us to convert text to speech
import datetime
import speech_recognition as sr     
import wikipedia
import webbrowser
import os
import pywhatkit as pykt
from keyboard import press_and_release

engine = pyttsx3.init('sapi5')              # Microsoft developed speech API
voices = engine.getProperty('voices')           # getting details of current voice
engine.setProperty('voice', voices[0].id)


def speak(audio2):
    engine.say(audio2)         
    engine.runAndWait()                     # Without this command, speech will not be audible to us.


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")

    else:
        speak("Good evening Sir")
    
    speak("Welcome back sir, how may I help")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    print("Listening.....")
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            #print("Recognizing.....")
            query = r.recognize_google(audio2)              # Using google for voice recognition.
            query = query.lower()
            print("You said: ", query)
            #speak(query)

    except sr.RequestError as e:
        print("Could not request")
    
    except sr.UnknownValueError:
        print("Can you say that again....")
        return "None"

    return query


if __name__ == "__main__":
    # To start or stop jarvis
    while(True):
        comd = takeCommand().lower()
        if 'wake up' in comd or 'are you there' in comd or 'switch on' in comd or 'listening' in comd:
            wishMe()
            jarvis = 1
            # Logic for executing tasks based on query
            while(jarvis):

                #print("query: ")
                #query = input()
                query = takeCommand()

                if 'wikipedia' in query:                # To listen summary of wikipedia of query
                    speak('Searching wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak('According to Wikipedia')
                    print(results)
                    speak(results)

                elif 'the time' in query:               # to tell the time
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")

                # Automating chrome
                elif 'google' in query:                 
                    query = query.replace("google", "")
                    speak("This is what I found in google")
                    pykt.search(query)

                elif 'history' in query:
                    speak("current history of your google chrome")
                    press_and_release('ctrl+h')

                elif 'downloads' in query:
                    speak("current downloads of your google chrome")
                    press_and_release('ctrl+j')

                elif 'close all tab' in query:
                    speak("Closing all the tab")
                    press_and_release('ctrl+shift+w')

                elif 'close' in query and 'tab' in query:
                    speak("Closing the tab")
                    press_and_release('ctrl+w')


                # Automating youtube
                elif 'play' in query and 'on youtube' in query:
                    query = query.replace("on youtube", "")
                    query = query.replace("play", "")
                    speak("Yes sir, This is what I found")
                    web = "https://www.youtube.com/results?search_query=" + query
                    webbrowser.open(web)
                    speak("Starting the first video")
                    pykt.playonyt(query)            


                # Automating system applications
                elif 'downloads in system' in query:
                    download_dir = 'C:\\Users\\Narauttam Singh\\Downloads'
                    download_list = os.listdir(download_dir)
                    print(download_list)

                elif 'open code' in query:
                    codePath = "C:\\Users\\Narauttam Singh\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)
                
                # Switch to next application
                elif 'switch' in query:
                    press_and_release('alt+tab') 
            
                # closing jarvis to not work on these logics
                elif 'exit' in query:
                    print('I am leaving')
                    speak('Ok Thank you sir')
                    jarvis = 0
                        
        elif 'shutdown' in comd or 'shut down' in comd or 'kill' in comd or 'switch off' in comd:
            speak("Yes sir, I will sleep now")
            exit()
