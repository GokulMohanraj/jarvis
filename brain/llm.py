import requests

from config.settings import (
    OLLAMA_URL,
    MODEL_NAME
)

from memory.session_memory import get_history

def ask_jarvis(prompt: str):

    history = get_history()

    context = ""

    for message in history:
        context += f"{message['role']}: {message['content']}\n"

    full_prompt = f"""
    Previous Conversation:

    {context}

    User: {prompt}

    Assistant:
    """

    payload = {
        "model": MODEL_NAME,
        "prompt": full_prompt,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    data = response.json()

    return data["response"]