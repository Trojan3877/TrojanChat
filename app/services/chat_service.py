import logging

from app.core.inference_cache import get_cached, make_cache_key, set_cached
from app.core.prompt_templates import CHAT_PROMPT

logger = logging.getLogger(__name__)


class ChatService:
    def __init__(self, llm_client):
        self.llm = llm_client

    def respond(self, history: str, user_input: str) -> str:
        key = make_cache_key(history, user_input)
        cached = get_cached(key)
        if cached is not None:
            logger.info("inference_cache_hit cache_key=%s", key)
            return cached

        prompt = CHAT_PROMPT.format(
            conversation=history,
            user_input=user_input
        )
        result = self.llm.generate(prompt)
        set_cached(key, result)
        return result
