import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    
    print("dime un mensaje")

    r.adjust_for_ambient_noise(source)

    audio = r.listen(source)
    try:
        comando = r.recognize_google(audio, language='es-ES')
        print(f"Este es tu mensaje: {comando}")
    except sr.UnknownValueError:
        print("No se entendio el mensaje")
    except sr.RequestError as e:
        print(f"hay un error en {e}")

    

