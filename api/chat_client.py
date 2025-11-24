import socket

class ChatClient:
    def __init__(self, host="server", port=9000):
        self.host = host
        self.port = port

    def send_message(self, text: str):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((self.host, self.port))
            client.sendall(text.encode("utf-8"))
            client.close()
            return True
        except Exception as e:
            return {"error": str(e)}