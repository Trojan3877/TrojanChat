import pytest
from mcp_adapter import handle_mcp_request, CHAT_HISTORY


def test_send_message_success():
    payload = {
        "room": "game-day",
        "user": "Corey",
        "message": "Fight On! Touchdown Trojans! 🏈🔥"
    }
    result = handle_mcp_request("send_message", payload)

    assert result["status"] == "sent"
    assert "timestamp" in result
    assert any(msg["message"] == "Fight On! Touchdown Trojans! 🏈🔥" for msg in CHAT_HISTORY["game-day"])


def test_fetch_messages_limit():
    # Ensure some messages exist
    handle_mcp_request("send_message", {
        "room": "recruiting",
        "user": "Fan123",
        "message": "New 5-star QB commit confirmed!"
    })

    result = handle_mcp_request("fetch_messages", {
        "room": "recruiting",
        "limit": 1
    })

    assert isinstance(result, list)
    assert len(result) == 1
    assert "user" in result[0]
    assert "message" in result[0]


def test_invalid_room_send():
    payload = {
        "room": "not-a-room",
        "user": "TestUser",
        "message": "Hello?"
    }
    result = handle_mcp_request("send_message", payload)
    assert result["status"] == "failed"


def test_invalid_tool():
    payload = {
        "room": "game-day",
        "user": "Corey",
        "message": "Invalid tool test"
    }
    result = handle_mcp_request("invalid_tool", payload)
    assert "error" in result
    assert "Unknown tool" in result["error"]
