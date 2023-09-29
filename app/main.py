from fastapi import APIRouter, FastAPI

from app.config import config
from app.lots.routes import router as lots_router
from app.users.routes import router as users_router
from dependencies import load_fastapi_dependencies

app = FastAPI(debug=config.DEBUG)
load_fastapi_dependencies(app)

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


router.include_router(lots_router, prefix="/lots")
router.include_router(users_router, prefix="/users")
app.include_router(router)
