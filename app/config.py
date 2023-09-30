from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseSettings):
    DEBUG: bool = False

    SECRET_KEY: str

    DATABASE_DRIVER: str = "postgresql+asyncpg"
    DATABASE_NAME: str = "postgres"
    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int = 5432
    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: str = "postgres"

    RABBITMQ_HOST: str = "rabbitmq"
    RABBITMQ_PORT: str = 5672

    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int = 465
    MAIL_SERVER: str

    @property
    def database_url(self) -> str:
        return (
            f"{self.DATABASE_DRIVER}://"
            f"{self.DATABASE_USER}:"
            f"{self.DATABASE_PASSWORD}@"
            f"{self.DATABASE_HOST}/"
            f"{self.DATABASE_NAME}"
        )

    @property
    def rabbitmq_amqp_url(self) -> str:
        return f"amqp://guest:guest@{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}"

    @property
    def rabbitmq_rpc_url(self) -> str:
        return f"rpc://guest:guest@{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}"


config = Config()
