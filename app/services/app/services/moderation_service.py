class ModerationService:
    def is_allowed(self, text: str) -> bool:
        banned_keywords = ["hate", "violence"]
        return not any(word in text.lower() for word in banned_keywords)