import pytest
from backend.services.chat_service import ChatService

@pytest.fixture
def chat_service():
    """Fixture to create a fresh ChatService for each test."""
    return ChatService()


def test_send_message(chat_service):
    """Test that a message is stored correctly."""
    msg = chat_service.send_message("Corey", "Fight On!")

    assert msg["username"] == "Corey"
    assert msg["content"] == "Fight On!"
    assert "id" in msg
    assert "timestamp" in msg


def test_get_messages_limit(chat_service):
    """Test that message history respects limit parameter."""
    for i in range(100):
        chat_service.send_message("User", f"Message {i}")

    messages = chat_service.get_messages(limit=10)

    assert len(messages) == 10
    assert messages[-1]["content"] == "Message 99"


def test_message_order(chat_service):
    """Test that messages are returned in chronological order."""
    chat_service.send_message("A", "First")
    chat_service.send_message("B", "Second")

    messages = chat_service.get_messages(limit=2)

    assert messages[0]["content"] == "First"
    assert messages[1]["content"] == "Second"
