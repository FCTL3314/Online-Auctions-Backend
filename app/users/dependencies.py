from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.users.managers import UserManager
from app.users.models import User
from dependencies import ActiveSession


async def get_user_db(
    session: AsyncSession = ActiveSession,
) -> AsyncGenerator[SQLAlchemyUserDatabase, None]:
    yield SQLAlchemyUserDatabase(session, User)


UserDB = Depends(get_user_db)


async def get_user_manager(user_db=UserDB) -> AsyncGenerator[UserManager, None]:
    yield UserManager(user_db)
