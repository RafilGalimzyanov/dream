from pydantic import BaseSettings, Field


class CommonSettings(BaseSettings):
    api_path: str = '/'


class Settings(BaseSettings):
    name: str = Field("admin", description="Наименование базы данных")
    user_name: str = Field("admin", description="Наименование пользователя")
    password: str = Field("root", description="Пароль")
    host: str = Field("localhost", description="Host")
    port: int = 5432


setting = Settings()
