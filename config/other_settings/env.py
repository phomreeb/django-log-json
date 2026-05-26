from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class EnvironmentSettings(BaseSettings):
    SECRET_KEY: str
    DEBUG: bool = False
    ALLOWED_HOSTS: str = "*"
    TIME_ZONE: str = "Asia/Bangkok"

    # Database Configuration
    DB_NAME: str = "postgres"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432

    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

env = EnvironmentSettings()
