import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)

    except:
        pass

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%H %p')
        talk(time)
        print(time)
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'single' in command:
        print('i am in a relationship with wifi')
        talk('i am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())



run_alexa()
