import asyncio
import httpx
import datetime
import os

API_URL = os.getenv("TROJANCHAT_API_URL", "http://localhost:8000")

# How often to refresh chat history (seconds)
REFRESH_INTERVAL = 2


def format_message(msg):
    """Pretty-print a message."""
    timestamp = msg["timestamp"].replace("T", " ").split(".")[0]
    return f"[{timestamp}] {msg['username']}: {msg['content']}"


async def fetch_messages(limit=20):
    """Fetch the latest chat messages from the backend."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{API_URL}/chat/history?limit={limit}")
            return response.json()
    except Exception as e:
        print(f"Error fetching messages: {e}")
        return []


async def send_message(username, content):
    """Send a message to the backend."""
    try:
        async with httpx.AsyncClient() as client:
            payload = {"username": username, "content": content}
            await client.post(f"{API_URL}/chat/send", json=payload)
    except Exception as e:
        print(f"Error sending message: {e}")


async def message_listener():
    """Continuously fetch messages and refresh the chat screen."""
    last_messages = []

    while True:
        messages = await fetch_messages()

        if messages != last_messages:
            os.system("cls" if os.name == "nt" else "clear")
            print("=== TrojanChat Terminal Client ===")
            print("Type your message below.\n")
            for msg in messages:
                print(format_message(msg))
            print("\n----------------------------------")
            last_messages = messages

        await asyncio.sleep(REFRESH_INTERVAL)


async def user_input(username):
    """Handle user input for sending messages."""
    while True:
        content = await asyncio.to_thread(input, "")
        if content.strip():
            await send_message(username, content)


async def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== TrojanChat Terminal Client ===")
    username = input("Enter your username: ").strip()

    if not username:
        print("Username cannot be empty.")
        return

    await asyncio.gather(
        message_listener(),
        user_input(username)
    )


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting TrojanChat...")
