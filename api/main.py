from fastapi import FastAPI
from pydantic import BaseModel

from brain.llm import ask_jarvis

from memory.session_memory import (
    add_message
)
from memory.session_memory import clear_history
from memory.session_memory import get_history

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Jarvis is running"}

@app.post("/chat")
def chat(request: ChatRequest):

    add_message(
        "user",
        request.message
    )

    response = ask_jarvis(      
        request.message
    )

    add_message(
        "assistant",
        response
    )

    return {
        "user": request.message,
        "jarvis": response
    }

@app.post("/memory/clear")
def clear_memory():

    clear_history()

    return {
        "message": "Session memory cleared"
    }

@app.get("/memory")
def memory():

    return get_history()