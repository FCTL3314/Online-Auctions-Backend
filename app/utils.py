from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import Row

from app.db import Base


def is_obj_exists_or_404(
    obj: Base | Row | None, message: str = "The object was not found."
) -> None:
    """
    Raise HTTPException with status code 404 if object is not exists.
    """
    if obj is None:
        raise HTTPException(detail=message, status_code=HTTPStatus.NOT_FOUND)


def is_response_match_object_fields(
    response_data: dict, obj: dict | object, fields: tuple | list
) -> bool:
    """
    Checks whether the fields of the obj are equal to the
    fields of the response_data parameter.
    """
    for field in fields:
        response_field = response_data[field]
        obj_field = str(obj[field] if isinstance(obj, dict) else getattr(obj, field))
        if response_field != obj_field:
            return False
    return True
