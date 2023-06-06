import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings, AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    database: str = os.getenv("DATABASE", 'default')
    # database_url: AnyUrl = os.environ.get("DATABASE_URL")
    # database_test_url: AnyUrl = os.environ.get("DATABASE_TEST_URL")
    POSTGRES_PORT: str = os.environ.get("POSTGRES_PORT")
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    # secret_key: str = os.environ.get("SECRET_KEY")
    FIRST_SUPERUSER: str = os.environ.get("FIRST_SUPERUSER")
    FIRST_SUPERUSER_PASSWORD: str = os.environ.get("FIRST_SUPERUSER_PASSWORD")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SECRET_KEY: str = os.environ.get("SECRET_KEY")



def get_settings() -> Settings:
    log.info("Loading config settings from the environment...")
    return Settings()