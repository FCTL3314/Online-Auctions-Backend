from fastapi_filter.contrib.sqlalchemy import Filter
from pydantic import Field

from app.lots.models import Lot


class LotFilter(Filter):
    title__in: list[str] | None = Field(alias="titles")

    class Constants(Filter.Constants):
        model = Lot

    class Config:
        populate_by_name = True
