from app.core.config import settings
from app.core.llm_client import LLMClient
from app.services.chat_service import ChatService

if not settings.openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable is required")

llm = LLMClient(api_key=settings.openai_api_key)
chat_service = ChatService(llm)
