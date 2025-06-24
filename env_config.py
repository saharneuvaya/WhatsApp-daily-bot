from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    TWILIO_SID: str
    TWILIO_AUTH_TOKEN: str
    FROM_WA: str
    TO_WA: str

    class Config:
        env_file = ".env"

settings = Settings()