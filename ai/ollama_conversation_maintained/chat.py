from ollama import chat
from config import (
  OLLAMA_MODEL
)
# from .config

class LlamaChat:
  def get_response(self, messages):
    response = chat(
        model=OLLAMA_MODEL, #commented out because wanted to see if config files could be removed
        # model="deepseek-r1",
        messages=messages,
    )
    return response.message.content