from fastapi import Depends, FastAPI
from fastapi_pagination import add_pagination

from app.db import get_session

ActiveSession = Depends(get_session)


def load_fastapi_dependencies(app: FastAPI) -> None:
    add_pagination(app)
