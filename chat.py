from openai import OpenAI
import pyttsx3


engine = pyttsx3.init()

engine.setProperty('voice','''HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0''')


client = OpenAI(
  api_key='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',  # this is also the default, it can be omitted
)

import speech_recognition as sr

r = sr.Recognizer()

historia_chat = []

def IA (prompt):


        historia_chat.append({"role":"user","content":prompt})

        respuesta = client.chat.completions.create(
            messages=historia_chat,
            model="gpt-3.5-turbo",
            stream=True,
            max_tokens=409
        )
        colecionMensaje = []


        for chunk in respuesta:
        
            chunk_message = chunk.choices[0].delta.content # extract the message
            colecionMensaje.append(chunk_message)  # save the message
            limpiarMensaje = [str(m) if m is not None else '' for m in colecionMensaje]
            mensajeComplecto = ''.join(limpiarMensaje)
            print(mensajeComplecto)
            #clear the terminal
            print("\033[H\033[J", end="")

            print(mensajeComplecto)
            historia_chat.append({"role":"assistant","content":mensajeComplecto})
        engine.say(mensajeComplecto)
        engine.runAndWait()

def Mensaje():
    while True:  
        with sr.Microphone() as source:
        
            print("dime un mensaje")

            r.adjust_for_ambient_noise(source)

            audio = r.listen(source)
            try:
                comando = r.recognize_google(audio, language='es-ES')
                print(f"Este es tu mensaje: {comando}")
                if(comando != 'salir' or comando != "Salir"):
                    IA(comando)
                else:
                     break
            except sr.UnknownValueError:
                print("No se entendio el mensaje")
            except sr.RequestError as e:
                print(f"hay un error en {e}")


Mensaje()