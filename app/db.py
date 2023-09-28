from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.ext.declarative import declarative_base

from app.config import config

Base = declarative_base()

engine = create_async_engine(config.database_url)
session_maker = async_sessionmaker(bind=engine, class_=AsyncSession)


async def get_session() -> AsyncGenerator:
    async with session_maker() as session:
        yield session
