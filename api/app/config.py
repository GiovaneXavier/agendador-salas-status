from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite+aiosqlite:///./room_status.db"
    booking_api_url: str = "http://localhost:8000/api"
    booking_api_token: str = ""
    webhook_secret: str = ""  # deixar vazio desativa a autenticação (modo dev)

    class Config:
        env_file = ".env"


settings = Settings()
