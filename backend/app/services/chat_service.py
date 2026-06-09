from ai.graph.langgraph_flow import TrojanChatAI

class ChatService:
    def __init__(self):
        self.ai = TrojanChatAI()

    def process_message(self, message: str):
        return self.ai.run(message)