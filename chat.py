from openai import OpenAI, AsyncOpenAI
import pyttsx3
engine = pyttsx3.init()

engine.setProperty('voice','''HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0''')

# for voice in engine.getProperty('voice'):
#     print(voice)

client = OpenAI(
  api_key='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',  # this is also the default, it can be omitted
)

response_iterator = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "en una palabra define que es  AGI",
        }
    ],
    model="gpt-3.5-turbo",
    stream=True,
    max_tokens=10
)
collected_messages = []


for chunk in response_iterator:

    chunk_message = chunk.choices[0].delta.content # extract the message
    collected_messages.append(chunk_message)  # save the message
    cleaned_messages = [str(m) if m is not None else '' for m in collected_messages]
    full_reply_content = ''.join(cleaned_messages)
    print(full_reply_content)

    #clear the terminal
    print("\033[H\033[J", end="")

print(full_reply_content)
engine.say(full_reply_content)
engine.runAndWait()
