"""
Настройки проекта
"""

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Настройки проекта
    """
    model_config = SettingsConfigDict(extra='ignore',
                                      env_file=["env.sample", ".env"]
                                      )

    psql_uri_db: str  # строка соединения с БД


@lru_cache()
def get_settings():
    """
    Получение кэшированных настроек
    """
    return Settings()
