from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import Row

from app.db import Base


def is_obj_exists_or_404(obj: Base | Row | None, message: str = "The object was not found.") -> None:
    """
    Raise HTTPException with status code 404 if object is not exists.
    """
    if obj is None:
        raise HTTPException(detail=message, status_code=HTTPStatus.NOT_FOUND)
