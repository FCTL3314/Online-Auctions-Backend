import asyncio
from typing import AsyncGenerator, Generator

import pytest
from httpx import AsyncClient
from mixer.auto import mixer
from sqlalchemy.engine import Row
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from app.db import Base, get_session
from app.lots.models import Lot
from app.main import app

test_engine = create_async_engine("sqlite+aiosqlite:///:memory:")
test_session_maker = async_sessionmaker(bind=test_engine, class_=AsyncSession)
Base.metadata.bind = test_engine


async def override_get_session() -> AsyncGenerator:
    async with test_session_maker() as session:
        yield session


app.dependency_overrides[get_session] = override_get_session  # noqa


@pytest.fixture(autouse=True)
async def prepare_database() -> None:
    """
    Creates the test database when tests run, deletes
    when tests finished.
    """
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="session")
def event_loop(request) -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def session() -> AsyncGenerator[AsyncSession, None]:
    async with test_session_maker() as session:
        yield session


@pytest.fixture(scope="session")
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as async_client:
        yield async_client


async def create_test_object(model_path: str, session: AsyncSession, **kwargs) -> Base:
    """
    Creates a test object that will be deleted when
    the test is complete.
    """
    obj = mixer.blend(model_path, **kwargs)
    session.add(obj)
    await session.commit()
    await session.refresh(obj)
    return obj


async def remove_test_object(obj: Base | Row | None, session: AsyncSession) -> None:
    await session.delete(obj)
    await session.commit()


@pytest.fixture()
async def lot(session: AsyncSession) -> AsyncGenerator[Base, None]:
    lot = await create_test_object("app.lots.models.Lot", session)
    yield lot
    await remove_test_object(lot, session)


@pytest.fixture()
async def bid(lot: Lot, session: AsyncSession) -> AsyncGenerator[Base, None]:
    submenu = await create_test_object("app.lots.models.Bid", session, lot_id=lot.id)
    yield submenu
    await remove_test_object(submenu, session)


@pytest.fixture()
async def user(session: AsyncSession) -> AsyncGenerator[Base, None]:
    user = await create_test_object("app.users.models.User", session)
    yield user
    await remove_test_object(user, session)
