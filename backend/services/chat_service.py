import uuid
import datetime
from backend.config import settings


class ChatService:
    """
    Chat service responsible for sending and retrieving messages.
    Currently uses in-memory storage, but the class is designed
    to be upgraded easily to Firebase, Redis, or SQL.
    """

    def __init__(self):
        # Temporary in-memory message store
        # Structure: { "id": str, "username": str, "content": str, "timestamp": str }
        self.messages = []

    def _generate_message_id(self):
        """
        Creates a unique message ID using UUID4.
        """
        return str(uuid.uuid4())

    def _timestamp(self):
        """
        Returns an ISO 8601 timestamp.
        """
        return datetime.datetime.utcnow().isoformat()

    # -------------------------------------
    #  PUBLIC METHODS
    # -------------------------------------

    def send_message(self, username: str, content: str):
        """
        Stores a chat message and returns the structured message.
        """
        message = {
            "id": self._generate_message_id(),
            "username": username,
            "content": content,
            "timestamp": self._timestamp(),
        }

        # In-memory storage (can replace with Firebase/Postgres/etc.)
        self.messages.append(message)

        return message

    def get_messages(self, limit: int = 50):
        """
        Returns the latest 'limit' chat messages.
        """
        return self.messages[-limit:]
