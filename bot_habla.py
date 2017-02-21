# -*- coding: utf-8 -*-
import pyttsx

engine = pyttsx.init()
engine.setProperty('rate', 130)    # Aquí puedes seleccionar la velocidad de la voz
engine.setProperty('voice', 'spanish')

def habla(texto):
    engine.say(texto)
    engine.runAndWait()

habla("Que quieres que te diga?")
while(1):
    frase_decir = raw_input("--> ")
    if (frase_decir == "exit"):
        exit(0)
    habla(frase_decir)
