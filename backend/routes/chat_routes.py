from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.services.chat_service import ChatService

router = APIRouter()

chat_service = ChatService()

# -------------------------------------------
#  Pydantic Models (request/response schemas)
# -------------------------------------------

class MessageRequest(BaseModel):
    username: str
    content: str


class MessageResponse(BaseModel):
    id: str
    username: str
    content: str
    timestamp: str


# -------------------------------------------
#  Routes
# -------------------------------------------

@router.post("/send", response_model=MessageResponse)
async def send_message(message: MessageRequest):
    """
    Sends a chat message to the realtime storage layer.
    """
    try:
        new_message = chat_service.send_message(
            username=message.username,
            content=message.content
        )
        return new_message
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history")
async def get_message_history(limit: int = 50):
    """
    Returns the latest N chat messages.
    """
    try:
        messages = chat_service.get_messages(limit=limit)
        return messages
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
