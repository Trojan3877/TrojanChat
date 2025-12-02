import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    """
    Centralized configuration for the TrojanChat backend.
    This allows clean environment separation and avoids hardcoding.
    """

    # App Settings
    APP_NAME: str = "TrojanChat Backend"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    # Backend API Version
    API_VERSION: str = "v1"

    # Firebase / Realtime Database Config (future)
    FIREBASE_API_KEY: str = os.getenv("FIREBASE_API_KEY", "")
    FIREBASE_PROJECT_ID: str = os.getenv("FIREBASE_PROJECT_ID", "")
    FIREBASE_DB_URL: str = os.getenv("FIREBASE_DB_URL", "")

    # Websocket / Realtime Layer
    USE_FIREBASE: bool = os.getenv("USE_FIREBASE", "true").lower() == "true"

    # Local development settings
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))

settings = Settings()
