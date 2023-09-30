from datetime import datetime

from pydantic import BaseModel

from app.bids.schemas import Bid


class Lot(BaseModel):
    id: int
    title: str
    description: str
    starting_price: float
    end_time: datetime


class LotWithBids(Lot):
    bids: list[Bid] = []


class LotCreate(Lot):
    id: int | None = None  # type: ignore[assignment]
    end_time: datetime | None = None  # type: ignore[assignment]
