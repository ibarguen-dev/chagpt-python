import pyttsx3
engine = pyttsx3.init()
for voice in engine.getProperty('voice'):
    print(voice)

