from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Message(BaseModel):
    user: str
    text: str


@app.post("/send")
def send(msg: Message):
    return {"status": "sent", "detail": f"{msg.user}: {msg.text}"}