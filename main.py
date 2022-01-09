import speech_recognition as spr
import pyttsx3

def asistente():

    escuchando = spr.Recognizer()

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

    try:
        with spr.Microphone() as microfono:
            print("... Escuchando...")
            voz = escuchando.listen(microfono)
            peticion = escuchando.recognize_google(voz)  # Api de google
            reconocimiento(peticion)

    except:
        pass


if __name__ == '__main__':
    asistente()
