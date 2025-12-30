from app.core.llm_client import LLMClient

class DummyClient:
    def responses(self): pass

def test_llm_client_interface():
    client = LLMClient(api_key="test")
    assert hasattr(client, "generate")