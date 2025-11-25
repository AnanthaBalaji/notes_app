from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Notes App"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings() 