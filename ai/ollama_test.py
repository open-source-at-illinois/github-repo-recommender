from ollama import chat

while(True):
  message = input("Give an input")
  stream = chat(
      model='llama3.2',
      messages=[{'role': 'user', 'content': message}],
      stream=True,
  )

  for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
