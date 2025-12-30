from app.services.chat_service import ChatService

class MockLLM:
    def generate(self, prompt):
        return "mock response"

def test_chat_service_response():
    service = ChatService(MockLLM())
    assert service.respond("", "hello") == "mock response"