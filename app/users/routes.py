from fastapi import APIRouter

from app.users.dependencies import fastapi_users
from app.users.auth import auth_backend
from app.users.constants import AUTH_TAG
from app.users.schemas import UserRead, UserCreate

router = APIRouter()

router.include_router(fastapi_users.get_auth_router(auth_backend), tags=[AUTH_TAG])
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate), tags=[AUTH_TAG]
)
