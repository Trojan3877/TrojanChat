import pytest
from websockets import connect

WS_URL = "ws://localhost:8000/ws/chat"

@pytest.mark.asyncio
async def test_websocket_connection():
    async with connect(WS_URL) as websocket:
        await websocket.send('{"username":"test","content":"hello"}')
        response = await websocket.recv()
        assert "hello" in response
