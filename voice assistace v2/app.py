import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print(" Not Understand")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':


    #if "hello jarvis" in sptext().lower():
        while True:
            data1=sptext().lower()
 
            if "your name" in data1:
                name = "my name is jarvis"
                speechtx(name)

            elif "what's your age" in data1:
                age = "I am a robot, so I do not age like humans. According to my data, I was created just a few minutes ago."
                speechtx(age)

            elif "what is time right now" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)

            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")

            elif 'google' in data1:
                webbrowser.open("https://www.google.com/")

            elif 'chat GPT' in data1:
                 webbrowser.open("https://chat.openai.com/")

            elif 'Netflix' in data1:
                 webbrowser.open("https://www.netflix.com/pk/")

            elif "jokes" in data1:
                 joke_1 = pyjokes.get_joke(language="en",category="neutral")
                 speechtx(joke_1)
                 print(joke_1)

            elif "play song" in data1:
                address = "E:\songs"
                listsong = os.listdir(address)
                print(listsong)
                os.startfile(os.path.join(address,listsong[0]))

            elif "exit" in data1:
                speechtx("thank you for joining this program")
                break

            time.sleep(5)
    #else:
    #    print("thank you")