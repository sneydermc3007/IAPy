import speech_recognition as spr
import pyttsx3
import time
import pywhatkit
from datetime import datetime
import wikipedia
import pyjokes


def asistente():
    escuchando = spr.Recognizer()
    nombre = 'catalina'

    IA = pyttsx3.init()
    voices = IA.getProperty('voices')
    """
    for voice in voices:
        print(voice)
    """
    IA.setProperty('voice', voices[1].id)

    IA.say("Hi Good morning, What do you need")
    IA.runAndWait()

    def reconocimiento(instruccion):
        IA.say(f'You told me you want {instruccion}')
        IA.runAndWait()

    def escucha():
        try:
            with spr.Microphone() as microfono:
                time.sleep(2)  # Espera en segundos
                print("... Escuchando...")
                voz = escuchando.listen(microfono)
                peticion = escuchando.recognize_google(voz)  # Api de google
                peticion = peticion.lower()
                print(peticion)

                if nombre in peticion:
                    peticion = peticion.replace(nombre, "")
                    print(peticion)

        except:
            pass

        return peticion

    def ejecuccion():
        """
        Todas las acciones que puede hacer la asistente virtual
        """
        peticion = escucha()
        if 'play' in peticion:
            print("\n ...Reproduciendo...")
            reconocimiento(peticion)

            IA.say("Playing")
            IA.runAndWait()

            peticion = peticion.replace('play ', '')
            time.sleep(5)
            pywhatkit.playonyt(peticion)

        elif 'what time is it' in peticion:
            print("\n ...Hora...")
            reconocimiento(peticion)

            hora = datetime.now().strftime('%H:%M:%S')
            print(hora)
            time.sleep(2.5)

            IA.say(f'The time is {hora}')
            IA.runAndWait()

        elif 'what day is today' in peticion:
            print("\n ...Dia...")
            reconocimiento(peticion)

            fecha = datetime.now().strftime('%Y-%m-%d')
            print(fecha)
            time.sleep(2.5)

            IA.say(f'Today is {fecha}')
            IA.runAndWait()

        elif 'search' in peticion:
            print("\n ...Buscando...")
            reconocimiento(peticion)

            IA.say("Searching")
            IA.runAndWait()
            time.sleep(1.5)

            peticion = peticion.replace('search ', '')
            informacion = wikipedia.summary(peticion, 1)

            IA.say(informacion)
            IA.runAndWait()

        elif 'joke' in peticion:
            print("\n ...Chiste...")
            reconocimiento(peticion)

            IA.say("Here I Go")
            IA.runAndWait()

            print(pyjokes.get_joke(language="es", category="all"))

            time.sleep(2)
            IA.say(pyjokes.get_joke())
            IA.runAndWait()

        else:
            print("\n ...Error...")

            IA.say("Sorry, please repeat the instruction")
            IA.runAndWait()
            asistente()

    ejecuccion()


if __name__ == '__main__':
    asistente()