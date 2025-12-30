from openai import OpenAI

class LLMClient:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def generate(self, prompt: str, temperature: float = 0.4) -> str:
        response = self.client.responses.create(
            model="gpt-4.1",
            input=prompt,
            temperature=temperature
        )
        return response.output_text