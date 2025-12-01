import os
import time
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
import pygame
from google import genai

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "AIzaSyB4n0r6sJhx-BQCFMjcuzldKhojNtblRV8")

if GOOGLE_API_KEY == "AIzaSyB4n0r6sJhx-BQCFMjcuzldKhojNtblRV8":
    print("JARVIS PROGRAM STARTED")

client = genai.Client(api_key=GOOGLE_API_KEY)
MODEL_NAME = "gemini-2.5-flash"

newsapi = "ee16bdcaecdd4d33bbe8ceafb52bed95"

# SPEAK FUNCTION
def speak(text):
    try:
        tts = gTTS(text=text, lang="en")
        tfile = "jarvis_temp.mp3"
        tts.save(tfile)

        pygame.mixer.init()
        pygame.mixer.music.load(tfile)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()
        os.remove(tfile)

    except Exception as e:
        print("TTS Error:", e)
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

def aiProcess(command):
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[
                {
                    "role": "user",
                    "parts": [
                        {"text": f"You are Jarvis. Reply in one short sentence.\nUser: {command}"}
                    ]
                }
            ]
        )

        return response.text.strip()

    except Exception as e:
        print("Gemini Error:", e)
        return "Sorry, I cannot respond right now."

# COMMAND HANDLER

def processCommand(c):
    c = c.lower()

    if "open google" in c:
        speak("Opening Google.")
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        speak("Opening YouTube.")
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c:
        speak("Opening Facebook.")
        webbrowser.open("https://facebook.com")

    elif "open linkedin" in c:
        speak("Opening LinkedIn.")
        webbrowser.open("https://linkedin.com")

    elif c.startswith("play "):
        song = c.replace("play ", "")
        link = musicLibrary.music.get(song)
        if link:
            speak(f"Playing {song}.")
            webbrowser.open(link)
        else:
            speak("I couldn't find that song.")

    elif "news" in c:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            data = r.json()
            articles = data.get("articles", [])[:5]

            if not articles:
                speak("No news available.")
            else:
                speak("Top headlines are:")
                for article in articles:
                    speak(article["title"])

        except:
            speak("Sorry, I cannot load the news right now.")

    else:
        reply = aiProcess(c)
        speak(reply)


# MAIN LOOP
if __name__ == "__main__":
    speak("Jarvis assistant activated.")

    recognizer = sr.Recognizer()

    while True:
        print("\nListening for wake word: 'Jarvis'...")

        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=6, phrase_time_limit=3)

            try:
                word = recognizer.recognize_google(audio)
                print("Heard:", word)
            except:
                continue

            if word.lower() == "jarvis":
                speak("Yes?")

                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source, timeout=8, phrase_time_limit=6)

                try:
                    command = recognizer.recognize_google(audio)
                    print("Command:", command)
                    processCommand(command)

                except Exception as e:
                    print("Command Error:", e)
                    speak("Say that again.")

        except KeyboardInterrupt:
            speak("Jarvis Deactivated.")
            break

        except Exception as e:
            print("Error:", e)
            time.sleep(1)
