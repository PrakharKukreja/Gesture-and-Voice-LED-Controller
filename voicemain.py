import pyttsx3
import speech_recognition as sr
import voicecontroller as cnt

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello I am Prakhar Kukreja")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening")
        print("Listening..........")
        audio=r.listen(source)
        try:
            print("Recognize.........")
            query=r.recognize_google(audio, language='en-in')
        except Exception as e:
            speak("Try Again")
            print("Try Again.......")
            return "None"
        return query 

if __name__=="__main__":
    while True:
        query=takeCommand().lower()
        if 'light on' in query:
            print("Turning Light On.....")
            speak("Turning Light On.....")
            cnt.led(1)
        elif 'light off' in query:
            print("Turning Lights Off......")
            speak("Turning Lights Off.......")
            cnt.led(0)
        elif 'exit' in query:
            break        
