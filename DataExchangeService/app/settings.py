from pydantic import BaseSettings, Field


class CommonSettings(BaseSettings):
    api_path: str = '/'


class Settings(BaseSettings):
    name: str = Field("db", description="Наименование базы данных")
    user: str = Field(description="Наименование пользователя")
    password: str = Field(description="Пароль")
    host: str = Field(description="Host")
    port: int = 5432


setting = Settings()
