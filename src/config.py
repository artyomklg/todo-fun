from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///todos.db"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30
    SECRET_KEY: str = 'very_secret_key'
    ALGORITHM: str = 'HS256'


settings: Settings = Settings()


if __name__ == '__main__':
    print(settings.model_dump())
