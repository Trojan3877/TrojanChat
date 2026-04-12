from unittest.mock import MagicMock, patch
import pytest

from ai.llm.groq_client import GroqClient


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_completion(text: str):
    """Build a minimal mock that looks like a Groq completion object."""
    message = MagicMock()
    message.content = text

    choice = MagicMock()
    choice.message = message

    usage = MagicMock()
    usage.prompt_tokens = 5
    usage.completion_tokens = 10
    usage.total_tokens = 15

    completion = MagicMock()
    completion.choices = [choice]
    completion.usage = usage
    return completion


def _make_stream_chunks(tokens: list):
    """Build a list of mock stream chunks."""
    chunks = []
    for token in tokens:
        delta = MagicMock()
        delta.content = token
        choice = MagicMock()
        choice.delta = delta
        chunk = MagicMock()
        chunk.choices = [choice]
        chunks.append(chunk)
    return chunks


# ---------------------------------------------------------------------------
# Instantiation tests
# ---------------------------------------------------------------------------

def test_groq_client_requires_api_key():
    """GroqClient raises ValueError when no API key is available."""
    with patch.dict("os.environ", {}, clear=True):
        with pytest.raises(ValueError, match="GROQ_API_KEY"):
            GroqClient(api_key=None)


def test_groq_client_accepts_explicit_key():
    """GroqClient can be instantiated with an explicit api_key."""
    with patch("ai.llm.groq_client.Groq"):
        client = GroqClient(api_key="test-key")
        assert client.api_key == "test-key"


def test_groq_client_reads_key_from_env():
    """GroqClient falls back to the GROQ_API_KEY environment variable."""
    with patch.dict("os.environ", {"GROQ_API_KEY": "env-key"}):
        with patch("ai.llm.groq_client.Groq"):
            client = GroqClient()
            assert client.api_key == "env-key"


# ---------------------------------------------------------------------------
# generate_response tests
# ---------------------------------------------------------------------------

def test_generate_response_sends_prompt():
    """generate_response returns a successful dict with the model's reply."""
    with patch("ai.llm.groq_client.Groq") as MockGroq:
        mock_create = MockGroq.return_value.chat.completions.create
        mock_create.return_value = _make_completion("Hello from Groq!")

        client = GroqClient(api_key="test-key")
        result = client.generate_response("Say hello")

        assert result["success"] is True
        assert result["response"] == "Hello from Groq!"
        assert "model" in result
        assert "usage" in result


def test_generate_response_includes_system_prompt():
    """generate_response prepends a system message when system_prompt is given."""
    with patch("ai.llm.groq_client.Groq") as MockGroq:
        mock_create = MockGroq.return_value.chat.completions.create
        mock_create.return_value = _make_completion("OK")

        client = GroqClient(api_key="test-key")
        client.generate_response("Hi", system_prompt="You are helpful.")

        call_args = mock_create.call_args
        messages = call_args.kwargs.get("messages") or call_args.args[0]
        roles = [m["role"] for m in messages]
        assert roles[0] == "system"
        assert roles[-1] == "user"


def test_generate_response_handles_api_error():
    """generate_response returns success=False when the API raises an exception."""
    with patch("ai.llm.groq_client.Groq") as MockGroq:
        MockGroq.return_value.chat.completions.create.side_effect = Exception("API error")

        client = GroqClient(api_key="test-key")
        result = client.generate_response("Trigger error")

        assert result["success"] is False
        assert "API error" in result["error"]


# ---------------------------------------------------------------------------
# stream_response tests
# ---------------------------------------------------------------------------

def test_stream_response_yields_tokens():
    """stream_response yields each content chunk from the API stream."""
    tokens = ["Hello", " ", "world"]
    with patch("ai.llm.groq_client.Groq") as MockGroq:
        MockGroq.return_value.chat.completions.create.return_value = (
            _make_stream_chunks(tokens)
        )

        client = GroqClient(api_key="test-key")
        result = list(client.stream_response("Hi"))

        assert result == tokens


def test_stream_response_handles_error():
    """stream_response yields an error string when the API raises an exception."""
    with patch("ai.llm.groq_client.Groq") as MockGroq:
        MockGroq.return_value.chat.completions.create.side_effect = Exception("stream fail")

        client = GroqClient(api_key="test-key")
        result = list(client.stream_response("Trigger error"))

        assert len(result) == 1
        assert "[ERROR]" in result[0]
        assert "stream fail" in result[0]
