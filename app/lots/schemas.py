from datetime import datetime

from pydantic import BaseModel


class Lot(BaseModel):
    id: int
    title: str
    description: str
    starting_price: float
    end_time: datetime


class LotCreate(Lot):
    id: int | None = None
    end_time: datetime | None = None
