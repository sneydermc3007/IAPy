import speech_recognition as spr
import pyttsx3
import time
import pywhatkit


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
        peticion = escucha()
        if 'play' in peticion:
            print("... Reproduciendo...")
            reconocimiento(peticion)

            peticion = peticion.replace('play', '')
            time.sleep(4)
            pywhatkit.playonyt(peticion)

    ejecuccion()


if __name__ == '__main__':
    asistente()