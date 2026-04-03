"""Tests for the Redis-backed inference cache."""

import importlib
import sys
import unittest.mock as mock

import pytest


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _reload_cache_module():
    """Reload inference_cache so module-level env vars are re-evaluated."""
    if "app.core.inference_cache" in sys.modules:
        del sys.modules["app.core.inference_cache"]
    return importlib.import_module("app.core.inference_cache")


# ---------------------------------------------------------------------------
# Cache-key stability
# ---------------------------------------------------------------------------

def test_make_cache_key_is_deterministic():
    from app.core.inference_cache import make_cache_key

    key1 = make_cache_key("hello", "world")
    key2 = make_cache_key("hello", "world")
    assert key1 == key2


def test_make_cache_key_differs_on_different_inputs():
    from app.core.inference_cache import make_cache_key

    assert make_cache_key("history A", "input A") != make_cache_key("history B", "input B")


def test_make_cache_key_includes_namespace():
    from app.core.inference_cache import make_cache_key

    key = make_cache_key("h", "u")
    assert key.startswith("trojan_chat:inference:")


# ---------------------------------------------------------------------------
# Cache hit behaviour
# ---------------------------------------------------------------------------

def test_get_cached_returns_value_on_hit(monkeypatch):
    from app.core import inference_cache

    fake_client = mock.MagicMock()
    fake_client.get.return_value = "cached response"
    monkeypatch.setattr(inference_cache, "_client", fake_client)
    monkeypatch.setattr(inference_cache, "CACHE_ENABLED", True)

    result = inference_cache.get_cached("some-key")

    assert result == "cached response"
    fake_client.get.assert_called_once_with("some-key")


def test_chat_service_returns_cached_result_without_calling_llm(monkeypatch):
    """ChatService.respond() must return the cached value and skip LLM."""
    from app.core import inference_cache
    from app.services.chat_service import ChatService

    fake_client = mock.MagicMock()
    fake_client.get.return_value = "cached llm answer"
    monkeypatch.setattr(inference_cache, "_client", fake_client)
    monkeypatch.setattr(inference_cache, "CACHE_ENABLED", True)

    llm_mock = mock.MagicMock()
    service = ChatService(llm_mock)
    result = service.respond("some history", "some input")

    assert result == "cached llm answer"
    llm_mock.generate.assert_not_called()


# ---------------------------------------------------------------------------
# Cache miss behaviour
# ---------------------------------------------------------------------------

def test_get_cached_returns_none_on_miss(monkeypatch):
    from app.core import inference_cache

    fake_client = mock.MagicMock()
    fake_client.get.return_value = None
    monkeypatch.setattr(inference_cache, "_client", fake_client)
    monkeypatch.setattr(inference_cache, "CACHE_ENABLED", True)

    result = inference_cache.get_cached("missing-key")
    assert result is None


def test_chat_service_calls_llm_on_cache_miss_and_stores_result(monkeypatch):
    """On a cache miss, ChatService must call the LLM and write to cache."""
    from app.core import inference_cache
    from app.services.chat_service import ChatService

    fake_client = mock.MagicMock()
    fake_client.get.return_value = None
    monkeypatch.setattr(inference_cache, "_client", fake_client)
    monkeypatch.setattr(inference_cache, "CACHE_ENABLED", True)

    llm_mock = mock.MagicMock()
    llm_mock.generate.return_value = "fresh llm answer"
    service = ChatService(llm_mock)
    result = service.respond("history", "user_input")

    assert result == "fresh llm answer"
    llm_mock.generate.assert_called_once()
    fake_client.setex.assert_called_once()


# ---------------------------------------------------------------------------
# Fail-open behaviour when Redis is unavailable
# ---------------------------------------------------------------------------

def test_get_cached_fails_open_on_redis_error(monkeypatch):
    """When Redis raises an exception, get_cached must return None (fail-open)."""
    from app.core import inference_cache

    fake_client = mock.MagicMock()
    fake_client.get.side_effect = ConnectionError("Redis is down")
    monkeypatch.setattr(inference_cache, "_client", fake_client)
    monkeypatch.setattr(inference_cache, "CACHE_ENABLED", True)

    result = inference_cache.get_cached("key")
    assert result is None


def test_set_cached_fails_open_on_redis_error(monkeypatch):
    """When Redis raises an exception, set_cached must not propagate the error."""
    from app.core import inference_cache

    fake_client = mock.MagicMock()
    fake_client.setex.side_effect = ConnectionError("Redis is down")
    monkeypatch.setattr(inference_cache, "_client", fake_client)
    monkeypatch.setattr(inference_cache, "CACHE_ENABLED", True)

    # Must not raise
    inference_cache.set_cached("key", "value")


def test_chat_service_still_returns_llm_answer_when_redis_is_down(monkeypatch):
    """Full flow: Redis errors must not prevent a valid LLM response."""
    from app.core import inference_cache
    from app.services.chat_service import ChatService

    fake_client = mock.MagicMock()
    fake_client.get.side_effect = ConnectionError("Redis is down")
    fake_client.setex.side_effect = ConnectionError("Redis is down")
    monkeypatch.setattr(inference_cache, "_client", fake_client)
    monkeypatch.setattr(inference_cache, "CACHE_ENABLED", True)

    llm_mock = mock.MagicMock()
    llm_mock.generate.return_value = "llm answer despite redis failure"
    service = ChatService(llm_mock)
    result = service.respond("history", "input")

    assert result == "llm answer despite redis failure"


# ---------------------------------------------------------------------------
# CACHE_ENABLED feature flag
# ---------------------------------------------------------------------------

def test_get_cached_skips_redis_when_cache_disabled(monkeypatch):
    from app.core import inference_cache

    fake_client = mock.MagicMock()
    monkeypatch.setattr(inference_cache, "_client", fake_client)
    monkeypatch.setattr(inference_cache, "CACHE_ENABLED", False)

    result = inference_cache.get_cached("key")

    assert result is None
    fake_client.get.assert_not_called()


def test_set_cached_skips_redis_when_cache_disabled(monkeypatch):
    from app.core import inference_cache

    fake_client = mock.MagicMock()
    monkeypatch.setattr(inference_cache, "_client", fake_client)
    monkeypatch.setattr(inference_cache, "CACHE_ENABLED", False)

    inference_cache.set_cached("key", "value")

    fake_client.setex.assert_not_called()
