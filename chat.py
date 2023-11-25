from openai import OpenAI, AsyncOpenAI

client = OpenAI(
  api_key='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',  # this is also the default, it can be omitted
)

response_iterator = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Dame ejemplos de un ciclo for en python",
        }
    ],
    model="gpt-3.5-turbo",
    stream=True,
    max_tokens=100,
)
collected_messages = []

# print(response_iterator)

for chunk in response_iterator:

    chunk_message = chunk['ChatCompletionChunk']['choices'][0]['message']['content']  # extract the message
    collected_messages.append(chunk_message)  # save the message
    full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
    print(full_reply_content)

    # clear the terminal
    print("\033[H\033[J", end="")

print(full_reply_content)

