from datetime import datetime

from pydantic import BaseModel


class Bid(BaseModel):
    id: int
    amount: float
    created_at: datetime
