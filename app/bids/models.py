from datetime import datetime
from decimal import Decimal

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class Bid(Base):
    __tablename__ = "bid"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[Decimal]

    lot_id: Mapped[int] = mapped_column(ForeignKey("lot.id"))
    lot = relationship("Lot", back_populates="bids")

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self):
        return f"Bid(id={self.id}, amount={self.amount})"
