from fastapi import APIRouter, FastAPI

from app.config import Config

app = FastAPI(debug=Config.DEBUG)
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


app.include_router(router)
