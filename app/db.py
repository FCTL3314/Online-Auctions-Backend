import asyncio
from asyncio import current_task
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)
from sqlalchemy.ext.declarative import declarative_base

from app.config import config

Base = declarative_base()

engine = create_async_engine(config.database_url)
session_maker = async_sessionmaker(bind=engine, class_=AsyncSession)


async def get_session() -> AsyncGenerator:
    async with session_maker() as session:
        yield session


@asynccontextmanager
async def scoped_session(async_session_maker=None):
    """
    Scoped session to run asynchronous tasks in Celery.
    """
    scoped_factory = async_scoped_session(
        async_session_maker,
        scopefunc=current_task,
    )
    try:
        async with scoped_factory() as session:
            yield session
    finally:
        await scoped_factory.remove()


scoped_loop = asyncio.new_event_loop()
