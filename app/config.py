from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseSettings):
    DEBUG: bool = False

    DATABASE_DRIVER: str = "postgresql+asyncpg"
    DATABASE_NAME: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str

    @property
    def database_url(self) -> str:
        return (
            f"{self.DATABASE_DRIVER}://"
            f"{self.DATABASE_USER}:"
            f"{self.DATABASE_PASSWORD}@"
            f"{self.DATABASE_HOST}/"
            f"{self.DATABASE_NAME}"
        )


config = Config()
