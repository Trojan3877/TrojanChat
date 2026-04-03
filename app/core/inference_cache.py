# app/core/inference_cache.py

import hashlib
import json
import logging
import os

import redis

logger = logging.getLogger(__name__)

CACHE_ENABLED: bool = os.getenv("CACHE_ENABLED", "true").lower() == "true"
CACHE_TTL: int = int(os.getenv("CACHE_TTL", "3600"))
REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")
MODEL_VERSION: str = os.getenv("MODEL_VERSION", "gpt-4.1")

_client: "redis.Redis | None" = None


def _get_client() -> "redis.Redis | None":
    """Return a (lazily-created) Redis client, or None if caching is disabled."""
    global _client
    if not CACHE_ENABLED:
        return None
    if _client is None:
        try:
            _client = redis.from_url(
                REDIS_URL,
                decode_responses=True,
                socket_connect_timeout=1,
                socket_timeout=1,
            )
        except Exception as exc:  # pragma: no cover
            logger.error("redis_connect_error error=%s", exc)
    return _client


def make_cache_key(history: str, user_input: str) -> str:
    """Return a deterministic cache key for the given inference inputs."""
    raw = json.dumps(
        {"model": MODEL_VERSION, "history": history, "user_input": user_input},
        sort_keys=True,
    )
    digest = hashlib.sha256(raw.encode()).hexdigest()
    return f"trojan_chat:inference:{digest}"


def get_cached(key: str) -> "str | None":
    """Return the cached inference result for *key*, or None on miss/error."""
    from app.core.metrics import cache_errors, cache_hits, cache_misses

    client = _get_client()
    if client is None:
        return None
    try:
        value = client.get(key)
        if value is not None:
            cache_hits.inc()
            logger.info("cache_hit cache_key=%s", key)
            return value
        cache_misses.inc()
        logger.info("cache_miss cache_key=%s", key)
        return None
    except Exception as exc:
        cache_errors.inc()
        logger.error("redis_get_error cache_key=%s error=%s", key, exc)
        return None


def set_cached(key: str, value: str, ttl: int = CACHE_TTL) -> None:
    """Store *value* in Redis under *key* with the given TTL (seconds)."""
    from app.core.metrics import cache_errors

    client = _get_client()
    if client is None:
        return
    try:
        client.setex(key, ttl, value)
    except Exception as exc:
        cache_errors.inc()
        logger.error("redis_set_error cache_key=%s error=%s", key, exc)
