import speech_recognition as sr 
import os 

frase = sr.Recognizer()

with sr.Microphone() as mic:
    while True:
        frase.adjust_for_ambient_noise(mic)
        print('Fala alguma coisa')
        audio = frase.listen(mic)
        texto = frase.recognize_google(audio, language='pt-br')
        print(texto)