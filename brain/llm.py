import requests

from config.settings import (
    OLLAMA_URL,
    MODEL_NAME
)

def ask_jarvis(prompt: str):

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    data = response.json()

    return data["response"]