from app.core.config import settings
from app.core.llm_client import LLMClient
from app.services.chat_service import ChatService
from app.api.chat_routes import ChatController

llm = LLMClient(api_key=settings.openai_api_key)
chat_service = ChatService(llm)
controller = ChatController(chat_service)
feat(core): add GPT-4.1 LLM core architecture and chat services