# ================================================
# TrojanChat — Real-Time Terminal Client (WebSocket)
# ================================================

import asyncio
import websockets
import json
import os
from datetime import datetime

# Detect backend automatically OR use env variable
API_HOST = os.getenv("TROJANCHAT_API_HOST", "localhost")
WS_URL = f"ws://{API_HOST}:8000/ws/chat"
HTTP_URL = f"http://{API_HOST}:8000"

# Format chat messages for display
def format_message(msg):
    timestamp = msg["timestamp"].replace("T", " ").split(".")[0]
    return f"[{timestamp}] {msg['username']}: {msg['content']}"


async def receive_messages(websocket):
    """Continuously receive messages from WebSocket."""
    while True:
        try:
            data = await websocket.recv()
            msg = json.loads(data)

            print(format_message(msg))
        except websockets.ConnectionClosedOK:
            print("\nDisconnected from server.")
            break
        except Exception as e:
            print(f"Receive error: {e}")
            break


async def send_messages(websocket, username):
    """Continuously send user input as chat messages."""
    while True:
        try:
            content = await asyncio.to_thread(input, "")
            if content.strip():
                msg = {
                    "username": username,
                    "content": content,
                    "timestamp": datetime.utcnow().isoformat()
                }
                await websocket.send(json.dumps(msg))
        except Exception as e:
            print(f"Send error: {e}")
            break


async def main():
    print("=== TrojanChat Terminal Client (Real-Time) ===")
    username = input("Enter username: ").strip()

    if not username:
        print("Username cannot be empty.")
        return

    async with websockets.connect(WS_URL) as websocket:
        print("\nConnected! You can now chat in real time.\n")

        # Launch both tasks: listening + sending
        await asyncio.gather(
            receive_messages(websocket),
            send_messages(websocket, username)
        )


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting TrojanChat...")
