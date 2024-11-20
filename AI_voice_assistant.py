import speech_recognition as sr
import pyttsx3
import pyaudio
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')

if len(voices) > 1:
    engine.setProperty('voices', voices[1].id)
else:
    engine.setProperty('voices', voices[0].id)

def engine_talk(text):
    print(f"Alexa is saying:{text}")
    engine.say(text)
    engine.runAndWait()

def user_command():
    try:
        with sr.Microphone() as src:
            listener.adjust_for_ambient_noise(src)
            print('Start Speaking!!')
            voice = listener.listen(src)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(f'User said: {command}')
                return command

    except Exception as e:
        print(f'Error: {e}')
        return ""

def run_alexa():
    command = user_command()

    if command:
        if 'play' in command:
            song = command.replace('play', '')
            engine_talk('Playing' + song)
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            engine_talk('The current time is ' + time)

        elif 'who is' in command:
            name = command.replace('who is', '')
            info = wikipedia.summary(name, 1)
            engine_talk(info)

        elif 'joke' in command:
            engine_talk(pyjokes.get_joke())
            
        elif 'stop' in command:
            sys.exit()

        else:
            engine_talk('I could not hear you properly')
            
    else:
        engine_talk('did not catch that. please speak again!!!')

while True:
    run_alexa()
            




    
    



 
