import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")


r = sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak("Hey brusky, what video should we watch?")
    print("Listening...")
    audio = r.listen(source)
    print("Thinking...")



try:
    words = r.recognize_google(audio)
    speak.Speak("Ok Master, let's look for " + r.recognize_google(audio))
    wb.open("https://www.youtube.com/results?search_query=" + words)

except sr.UnkownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Couldn't connect to internet.")
                
