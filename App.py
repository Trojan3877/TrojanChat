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
    @app.post("/send")
def send(msg: Message):
    result = chat_client.send_message(f"{msg.user}: {msg.text}")
    return {"status": "sent", "detail": result}