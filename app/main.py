from fastapi import APIRouter, FastAPI
from fastapi_users import FastAPIUsers

from app.config import config
from app.users.auth import auth_backend
from app.users.dependencies import get_user_manager
from app.users.models import User
from app.users.schemas import UserCreate, UserRead

app = FastAPI(debug=config.DEBUG)
router = APIRouter(prefix="/api/v1")


@router.get(
    "/ping",
    tags=["Utility"],
    description="Check if the server is running.",
)
async def ping():
    return {
        "msg": "pong",
    }


fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth/registration",
    tags=["auth"],
)
app.include_router(router)
