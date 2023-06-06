import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings, AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    database: str = os.getenv("DATABASE", 'default')
    POSTGRES_PORT: str = os.environ.get("POSTGRES_PORT")
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    FIRST_SUPERUSER: str = os.environ.get("FIRST_SUPERUSER")
    FIRST_SUPERUSER_PASSWORD: str = os.environ.get("FIRST_SUPERUSER_PASSWORD")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SECRET_KEY: str = os.environ.get("SECRET_KEY")



def get_settings() -> Settings:
    log.info("Loading config settings from the environment...")
    return Settings()

TORTOISE_ORM = {
    "connections": {
        "default": {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': os.environ.get("POSTGRES_APP_SERVER"),
                'user': os.environ.get("POSTGRES_USER"),
                'password': os.environ.get("POSTGRES_PASSWORD"),
                'database': os.environ.get("POSTGRES_DB")
            }
        }
    },
    "apps": {
        "models": {
            "models": ["app.db.models.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}