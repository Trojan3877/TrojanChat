class SessionManager:
    def __init__(self):
        self.sessions = {}

    def get_history(self, session_id: str) -> str:
        return self.sessions.get(session_id, "")

    def update_history(self, session_id: str, message: str):
        self.sessions[session_id] = self.sessions.get(session_id, "") + message