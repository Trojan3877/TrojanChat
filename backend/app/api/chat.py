from fastapi import APIRouter
from pydantic import BaseModel
from ai.graph.langgraph_flow import TrojanChatAI

router = APIRouter()
ai_engine = TrojanChatAI()


class ChatRequest(BaseModel):
    message: str


@router.post("/")
async def chat(request: ChatRequest):
    result = ai_engine.run(request.message)

    return {
        "response": result.get("response"),
        "success": result.get("success")
    }