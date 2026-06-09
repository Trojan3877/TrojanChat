import asyncio
import json
import sys

async def watch_for_messages(reader: asyncio.StreamReader):
    """Listens continuously for raw data packages arriving from the backend network."""
    try:
        while True:
            data = await reader.read(4096)
            if not data:
                print("\n[-] Connection lost. Server went offline.")
                break
            
            try:
                payload = json.loads(data.decode('utf-8'))
                # Redraw line buffers to prevent incoming traffic from overwriting user typing inputs
                print(f"\n[{payload.get('user')}] -> {payload.get('text')}")
                print("Your message: ", end="", flush=True)
            except json.JSONDecodeError:
                pass
    except asyncio.CancelledError:
        pass

async def send_messages(writer: asyncio.StreamWriter, username: str):
    """Captures standard input asynchronously and wraps strings into structured payloads."""
    loop = asyncio.get_event_loop()
    print("Handshake established. Enter '/exit' to drop out cleanly.")
    print("Your message: ", end="", flush=True)
    
    try:
        while True:
            # Delegate terminal input tracking to an isolated system thread pool
            user_input = await loop.run_in_executor(None, sys.stdin.readline)
            cleaned_text = user_input.strip()
            
            if not cleaned_text:
                print("Your message: ", end="", flush=True)
                continue
                
            if cleaned_text.lower() == '/exit':
                break

            message_packet = {
                "user": username,
                "text": cleaned_text
            }
            
            writer.write(json.dumps(message_packet).encode('utf-8'))
            await writer.drain()
    except asyncio.CancelledError:
        pass
    finally:
        writer.close()
        await writer.wait_closed()

async def main():
    # Fall back safely if entry arguments aren't specified during execution initialization
    username = sys.argv[1] if len(sys.argv) > 1 else input("Choose your chat handle: ").strip() or "Anonymous"
    
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 8888

    try:
        reader, writer = await asyncio.open_connection(SERVER_IP, SERVER_PORT)
        
        # Concurrently schedule standard input loops alongside socket read loops
        receive_task = asyncio.create_task(watch_for_messages(reader))
        send_task = asyncio.create_task(send_messages(writer, username))
        
        done, pending = await asyncio.wait(
            [receive_task, send_task],
            return_when=asyncio.FIRST_COMPLETED
        )
        
        for task in pending:
            task.cancel()
            
    except ConnectionRefusedError:
        print(f"[-] Network Error: Connection refused at socket endpoint address {SERVER_IP}:{SERVER_PORT}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting chat terminal client.")
