import speech_recognition as sr
import pyttsx3
import time
import datetime
import webbrowser

engine = pyttsx3.init()
def sptext():
        recognizer=sr.Recognizer()
        with sr.Microphone() as source:
                speechtx("listening")
                recognizer.adjust_for_ambient_noise(source)
                audio =recognizer.listen(source)
        try:  
            speechtx("recognizing")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print(" Not Understand ")
            speechtx("not understand")
            time.sleep(2)
            return sptext()

def speechtx(text):
    engine.say(text)
    engine.runAndWait()

def main():
    command = sptext()
    if 'Google' in command:
            speechtx("Hello! Sir how can I help you?")
       
    while True:

        if 'goodbye' in command:
             speechtx("Goodbye!")
             break
        elif 'self' in command:
              speechtx("developed bye Mr ganesh")
              break
        elif 'open web' in command:
            speechtx("openning!")
            web_open=webbrowser.open("https://www.cybersuccess.biz/") 
            break
        elif 'now time' in command:
            now=datetime.datetime.now()
            speechtx(now.strftime("%I%H%M%S"))
            time.sleep(1) 
            break
        elif 'bye' in command:
            speechtx('bye! sir have a nice day')                

if __name__ == "__main__":
    main()

    
            
            
            
            