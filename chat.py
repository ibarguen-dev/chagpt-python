from openai import OpenAI, AsyncOpenAI
import pyttsx3
engine = pyttsx3.init()

engine.setProperty('voice','''HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0''')


client = OpenAI(
  api_key='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',  # this is also the default, it can be omitted
)

historia_chat = []
while True: 
    prompt = input('Ingrese la pregunta')


    if prompt == "salir":
        break
    else:

        historia_chat.append({"role":"user","content":prompt})

        respuesta = client.chat.completions.create(
            messages=historia_chat,
            model="gpt-3.5-turbo",
            stream=True,
            max_tokens=10
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

