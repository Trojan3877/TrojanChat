from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from ai.graph.langgraph_flow import TrojanChatAI

router = APIRouter()

# Lazy singleton — not created at import time so tests can override via DI
_ai_engine: Optional[TrojanChatAI] = None


def get_ai_engine() -> TrojanChatAI:
    """Return the shared TrojanChatAI instance (created on first request)."""
    global _ai_engine
    if _ai_engine is None:
        _ai_engine = TrojanChatAI()
    return _ai_engine


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: Optional[str]
    success: bool


@router.post("/", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    engine: TrojanChatAI = Depends(get_ai_engine),
) -> ChatResponse:
    """
    Accepts a user message, runs the RAG pipeline, and returns an AI response.
    """
    if not request.message.strip():
        raise HTTPException(status_code=422, detail="Message cannot be empty.")

    result = engine.run(request.message)
    return ChatResponse(
        response=result.get("response"),
        success=bool(result.get("success")),
    )