from re import S
import tkinter as tk
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import os
import random
from pytube import Search, YouTube
import time

r = sr.Recognizer()

def record():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            speak("Anlayamadım")
        except sr.RequestError:
            speak("Sistemsel Hata.")
        return voice
    

    
def response(voice):
    if len(voice) > 0:
        speak(voice + " Parametresini Arıyorum, Bekle...")
        s = Search(voice)
        time.sleep(1.5)
        speak(s.results[0].title + " Başlıklı Videoyu İndiriyorum...")
        s.results[0].streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download("videos")
        speak(s.results[0].title + " Başlıklı Videoyu İndirdim.")

    

def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1,10000)
    file = 'audio' + str(rand) + '.mp3'
    tts.save(file)
    playsound(file,False)
    os.remove(file)

form = tk.Tk()

form.title('Voitube')
form.geometry('225x75')
form.resizable(False,False)
form.attributes('-toolwindow', True)

#label = tk.Label(form, text='Konuşmak için basın...')
#label.pack(pady=5)

speak('Aramamı istediğin şeyi söyle')

def buttonClick():
    voice = record()
    response(voice)



button = tk.Button(form, text='Konuş', command=buttonClick)
button.pack(pady=20)



form.mainloop()
