import pyttsx3

from openai import OpenAI

historia_chat = []

engine = pyttsx3.init()

client = OpenAI(
  api_key='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',  # this is also the default, it can be omitted
)

engine.setProperty('voice','''HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0''')

def IA (prompt):

    try:
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

    except Exception:
        
        print("hay un error "+ Exception)