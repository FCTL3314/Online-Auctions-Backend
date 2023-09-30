from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class Bid(BaseModel):
    id: int
    amount: Decimal
    created_at: datetime
    user_id: int


class BidCreate(Bid):
    id: int | None = None  # type: ignore[assignment]
    created_at: datetime | None = None  # type: ignore[assignment]
    user_id: int | None = None  # type: ignore[assignment]


class Lot(BaseModel):
    id: int
    title: str
    description: str
    starting_price: Decimal
    end_time: datetime


class LotWithBids(Lot):
    bids: list[Bid] = []


class LotCreate(Lot):
    id: int | None = None  # type: ignore[assignment]
    end_time: datetime | None = None  # type: ignore[assignment]
