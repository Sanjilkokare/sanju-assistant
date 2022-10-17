import os
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
from requests import get

 





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)





def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=3 and hour<=11:
        speak('good morning!')

    elif hour>=12 and hour<=16:
        speak('good afternoon!')

    elif hour>=16 and hour<=21:
        speak('good evening!')

    else:
        speak('good night!')


    speak('Sir I am sanju, tell me how may i help you')





def takeCommand():
    # it takes microphone input form the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-In')
        print(f"User said: {query}\n" )

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"

    return query

#def sendEmail(to,content):
    server = smtplib.SMTP('smpt.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com',)





if __name__ == '__main__':
    wishMe()
    while True:
        if 1:
        
            query = takeCommand().lower()
        # logic for executing task based on query

        if 'wikipedia' in query:
            speak('ok sir')
            speak('Searching Wikipedia...')
            query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'sanju open youtube' in query:
            speak('ok sir what should i search on youtube')
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            speak(cm)

        elif 'sanju open google' in query:
            speak('ok sir what should i search on google')
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            speak(cm)


        elif 'sanju open facebook' in query:
            speak('ok sir')
            webbrowser.open("www.facebook.com") 

        elif 'sanju open twitter' in query:
            speak('ok sir')
            webbrowser.open("www.twitter.com")   


        elif 'the time' in query:
            speak('ok sir')
            strTime = datetime.datetime.now().strftime('%H %M %S')
            speak(f"Sir, the time is{strTime}")

        elif 'sanju open notepad' in query:
            speak('ok sir')
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)


        elif 'sanju play music for me' in query:
            speak('ok sir')
            music_dir = "D:\\my music"
            songs = os.listdir(music_dir)

            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))


        
            

        elif 'sanju open code for me' in query:
            speak('ok sir')
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'who are you' in query:
            speak('my dear sir i am your personal assistant ')

        elif 'sanju what work you can do' in query:
            speak('i can do casual works for you such as giving info time open browsers xetra')

        elif 'sanju what is your age' in query:
            speak('sir i am immoorrrttaall')

        elif 'sanju who is your creator' in query:
            speak('sanjil sir is my creater')

        elif 'what you can do to your creator' in query:
            speak('i worship to hanuman that my creator alives with me')





        elif 'open command prompt' in query:
            speak('ok sir')
            os.system('start cmd')

        
        elif 'show my ip' in query:
            speak('ok sir')
            ip = get("https://api.ipify.org").text
            speak(f'your ip is {ip} ')
            print('Your ip',ip)

        
        

        
                 
        
        
    
        
        

        
        

        


        


            
        
        
        
        

        
 

        

        

        

        










