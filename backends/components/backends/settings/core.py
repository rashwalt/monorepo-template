from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://mono:mono@db:3306/mono?charset=utf8mb4" # データベース定義

    model_config = SettingsConfigDict(
        case_sensitive=True,
    )
