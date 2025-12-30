from app.services.chat_service import ChatService

class DummyLLM:
    def generate(self, prompt): return "test"

def test_chat_response():
    chat = ChatService(DummyLLM())
    assert chat.respond("", "hi") == "test"