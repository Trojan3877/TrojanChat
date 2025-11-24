from api.chat_client import ChatClient
from fastapi import FastAPI
from pydantic import BaseModel
from ai.llm_agent import LLMAgent
from ai.moderation import Moderator
from ai.embeddings import EmbeddingStore

app = FastAPI()
chat_client = ChatClient()
ai_agent = LLMAgent()
moderator = Moderator()
memory = EmbeddingStore()

class Message(BaseModel):
    user: str
    text: str

@app.post("/ask_ai")
def ask_ai(msg: Message):
    if not moderator.check(msg.text):
        return {"error": "Message flagged by moderation system."}

    memory.add(msg.text)

    reply = ai_agent.respond(msg.text, msg.user)
    return {"reply": reply}

@app.post("/similar")
def similar(msg: Message):
    return {"matches": memory.search(msg.text)}