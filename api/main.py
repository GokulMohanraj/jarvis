from fastapi import FastAPI
from pydantic import BaseModel

from brain.llm import ask_jarvis

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Jarvis is running"}

@app.post("/chat")
def chat(request: ChatRequest):

    response = ask_jarvis(request.message)

    return {
        "user": request.message,
        "jarvis": response
    }
