from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    environment: str = "dev"

    class Config:
        env_file = ".env"

settings = Settings()