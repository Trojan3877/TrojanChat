from backend.models.message import ChatMessage
from datetime import datetime

def test_message_model():
    msg = ChatMessage(
        username="corey",
        content="hello",
        timestamp=datetime.utcnow()
    )
    assert msg.username == "corey"
    assert msg.content == "hello"
