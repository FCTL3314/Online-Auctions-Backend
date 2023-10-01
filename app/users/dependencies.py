from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users import FastAPIUsers
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import ActiveSession
from app.users.auth import auth_backend
from app.users.managers import UserManager
from app.users.models import User


async def get_user_db(
    session: AsyncSession = ActiveSession,
) -> AsyncGenerator[SQLAlchemyUserDatabase, None]:
    yield SQLAlchemyUserDatabase(session, User)


UserDB = Depends(get_user_db)


async def get_user_manager(user_db=UserDB) -> AsyncGenerator[UserManager, None]:
    yield UserManager(user_db)


fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])


async def get_current_active_user():
    return fastapi_users.current_user(active=True)


ActiveUser = Depends(get_current_active_user)
