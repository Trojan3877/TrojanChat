from app.services.chat_service import ChatService
from app.services.moderation_service import ModerationService

class ChatController:
    def __init__(self, chat_service: ChatService):
        self.chat = chat_service
        self.moderation = ModerationService()

    def handle_message(self, history: str, user_input: str) -> str:
        if not self.moderation.is_allowed(user_input):
            return "Message violates community guidelines."
        return self.chat.respond(history, user_input)