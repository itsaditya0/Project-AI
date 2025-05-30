import os

import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        speak("Sorry, there was an error with the speech recognition service.")
        return None

def respond(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "what time is it" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}.")
    elif "open YouTube".lower() in command:
        webbrowser.open("HTTP://youtube.com")
        speak("opening youtube...")
    elif"open chat gpt".lower() in command:
        webbrowser.open("https://chatgpt.com/")
        speak("opening chatgpt...")
    elif"open wikipedia".lower() in command:
        webbrowser.open("https://www.wikipedia.org/")
        speak("opening wikipedia...")
    elif"open WhatsApp".lower() in command:
        webbrowser.open("https://web.whatsapp.com/")
        speak("opening whatsapp...")
    elif"tell me today's NEWS".lower() in command:
        webbrowser.open("https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en")
        speak("here is latest news for you..")
    elif"i want to play games".lower() in command:
        webbrowser.open("https://playhop.com/")
        speak("here is the website for you to play games")
    elif"i want to listen to music".lower() in command:
        webbrowser.open("https://music.youtube.com/")
        speak("here is the best site for you to listen to music")
    elif"i want study material".lower() in command:
        webbrowser.open("https://www.pw.live/exams/gate/gate-cse-notes/")
        speak("here is a site  suitable for you to take notes")
    elif"open google".lower() in command:
        webbrowser.open("https://google.com/")
        speak("opening google")

    elif "exit" in command:
        speak("Goodbye!")

        return True
    else:
        speak("Sorry, I don't understand that command.")
    return False


def main():
    speak("Hi, I'm your assistant. How can I help you today?")
    while True:
        command = listen()
        if command:
            if respond(command.lower()):
                break

if __name__ == "__main__":
    main()



