from app.core.prompt_templates import CHAT_PROMPT

class ChatService:
    def __init__(self, llm_client):
        self.llm = llm_client

    def respond(self, history: str, user_input: str) -> str:
        prompt = CHAT_PROMPT.format(
            conversation=history,
            user_input=user_input
        )
        return self.llm.generate(prompt)
