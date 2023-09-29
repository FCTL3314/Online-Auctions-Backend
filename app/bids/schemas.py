from pydantic import BaseModel


class Bid(BaseModel):
    id: int
    amount: float
