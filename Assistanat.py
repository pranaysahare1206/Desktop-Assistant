import datetime
import webbrowser
import speech_recognition as sr
import pyttsx3
import wikipedia
import os
from AppOpener import run


engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<10:
        speak('good morning')
    elif hour>=10 and hour<18:
        speak("good aftrenoon")
    else:
        speak("good evening")


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print(" 🎶 Listening.......")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print(" 👀 Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said :{query}\n")

    except Exception as e:
        print(e)
        print("can't understand say that again...")
        speak("Sorry but can't understand say that again...")
        return  "None"
    return query     #command take any read

if __name__ == "__main__":
    print("Pranay's virtual Assistant")
    wishme()
    speak("welcome to pranay's virtual Assistant")
    speak("what can i help you")

i=0
while i==0:
    query=takecommand().lower()



    if 'wikipedia' in query: 
        speak("seraching Wikipedia...")
        query=query.replace("wikipedia","")
        result=wikipedia.summary(query,sentences=2)
        speak("Acording to Wikipedia")
        print(result)
        speak((result))

    #BROWSER BASED TASKS.......

    elif 'open youtube' in query:
        query=query.replace("open youtube","")
        webbrowser.open("https://www.youtube.com/results?search_query="+query)
    elif 'play on youtube'in query:
        query=query.replace("on youtube","")
        webbrowser.open("https://www.youtube.com/results?search_query="+query)
    elif 'open google' in query:
        query = query.replace("open google", "")
        webbrowser.open(("https://www.google.com/search?q="+query))
    elif 'google for' in query:
        query = query.replace("google for", "")
        webbrowser.open(("https://www.google.com/search?q="+query))
    elif 'open instagram'in query:
        webbrowser.open("instagram.com")
    elif 'open spotify' in query:
        webbrowser.open("spotify.com")
    elif 'open whatsapp' in query:
        webbrowser.open("https://web.whatsapp.com")
    elif 'open facebook'in query:
        webbrowser.open("facebook.com")
    elif 'on youtube' in query:
        query=query.replace("youtube","")
        webbrowser.open("https://www.youtube.com/results?search_query="+query)
    elif 'news'in query:
        webbrowser.open("https://news.google.com/topstories")
    elif 'show me pranay' in query:
        webbrowser.open("https://me-qr.com/data/image-pack/37253648")

    elif 'do you know kunal' in query:
        speak(("yes kunal is your friend and you are in same college"))


    elif 'time'in query:
        strTime= datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")

    #SYSYTEM APPS BASED TASK.....

    elif 'open chrome'in query:
        cromepath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(cromepath)
    elif 'open firefox'in query:
        firefoxpath="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        os.startfile(firefoxpath)
    elif 'open pycharm' in query:
        pycharmpath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.1\\bin\\pycharm64.exe"
        os.startfile(pycharmpath)

    elif 'open notepad' in query:
        os.system('notepad')
    elif 'open camera'in query:
        os.system("start microsoft.windows.camera:")
    elif 'open excel' in query:
        query=query.replace("open","")
        run (f"{query}")
    elif 'open' in query:
        query=query.replace("open","")
        run (f"{query}")




    elif 'stop' in query:
        i=1
        print("thank you...")
        speak("thank you")
    elif 'band ho ja bhai' in query:
        i=1
        print("thank you...")
        speak("thank you")
    elif 'close' in query:
        i=1
        print("thank you...")
        speak("thank you")
    elif 'quite'in query:
        i=1
        print("Thank You....")
        speak("thank you")