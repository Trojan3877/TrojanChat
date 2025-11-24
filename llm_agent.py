class LLMAgent:
    def __init__(self, model="gpt-4.1"):
        self.model = model

    def respond(self, prompt: str) -> str:
        return f"[AI-{self.model}] Placeholder response to: {prompt}"