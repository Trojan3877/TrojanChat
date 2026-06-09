import asyncio
import json
import logging
import sys

# Configure production-grade structured logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] Server: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

class ProductionChatServer:
    def __init__(self, host: str = '0.0.0.0', port: int = 8888):
        self.host = host
        self.port = port
        self.active_connections = set()

    async def broadcast(self, message_dict: dict, exclude_writer: asyncio.StreamWriter = None):
        """Concurrently broadcasts a validated JSON payload to all active clients."""
        if not self.active_connections:
            return

        payload = json.dumps(message_dict).encode('utf-8')
        
        # Build non-blocking concurrent write tasks
        tasks = [
            self._safe_write(writer, payload)
            for writer in self.active_connections
            if writer != exclude_writer
        ]
        
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)

    async def _safe_write(self, writer: asyncio.StreamWriter, payload: bytes):
        """Executes defensive, error-isolated writes to a single client socket."""
        try:
            writer.write(payload)
            await writer.drain()
        except Exception as e:
            logging.debug(f"Write failure encountered. Removing client: {e}")
            await self.disconnect_client(writer)

    async def handle_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        """Manages the full network lifecycle of an incoming connection stream."""
        self.active_connections.add(writer)
        client_peer = writer.get_extra_info('peername')
        logging.info(f"Establishment success: Connection recognized from {client_peer}")

        try:
            while True:
                data = await reader.read(4096)
                if not data:
                    break # Client closed the connection stream cleanly
                
                try:
                    # Enforce strict syntax parsing boundaries
                    incoming_msg = json.loads(data.decode('utf-8'))
                    
                    # Core sanitization to prevent message string payload injection
                    sanitized_text = str(incoming_msg.get("text", "")).strip()
                    if not sanitized_text:
                        continue
                        
                    broadcast_payload = {
                        "user": str(incoming_msg.get("user", "Anonymous")).strip(),
                        "text": sanitized_text,
                        "timestamp": asyncio.get_event_loop().time()
                    }
                    
                    await self.broadcast(broadcast_payload, exclude_writer=writer)
                    
                except json.JSONDecodeError:
                    logging.warning(f"Protocol violation: Malformed packet dropped from {client_peer}")
                    continue

        except asyncio.CancelledError:
            pass
        except Exception as e:
            logging.error(f"Runtime processing exception for client {client_peer}: {e}")
        finally:
            await self.disconnect_client(writer)

    async def disconnect_client(self, writer: asyncio.StreamWriter):
        """Safely purges connection tracking arrays and cuts off hanging descriptors."""
        if writer in self.active_connections:
            self.active_connections.remove(writer)
            client_peer = writer.get_extra_info('peername')
            logging.info(f"Teardown complete: Connection severed for {client_peer}")
        try:
            writer.close()
            await writer.wait_closed()
        except Exception:
            pass

    async def start(self):
        """Spins up the core network listening loop."""
        server = await asyncio.start_server(self.handle_client, self.host, self.port)
        logging.info(f"Production Chat Engine actively listening on custom interface: tcp://{self.host}:{self.port}")
        async with server:
            await server.serve_forever()

if __name__ == "__main__":
    server_engine = ProductionChatServer()
    try:
        asyncio.run(server_engine.start())
    except KeyboardInterrupt:
        logging.info("Administrative SIGINT caught. Shutting down system modules cleanly.")
