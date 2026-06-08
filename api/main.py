from fastapi import FastAPI
from pydantic import BaseModel

from brain.llm import ask_jarvis

from memory.sqlite_memory import (
    add_message,
    get_history,
    clear_history
)

from memory.database import initialize_database

initialize_database()

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