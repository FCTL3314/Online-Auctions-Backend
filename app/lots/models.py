from datetime import datetime, timedelta

from _decimal import Decimal
from sqlalchemy import String, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base
from app.lots.constants import LOT_LIFE_TIME_SECONDS


def lot_end_time() -> datetime:
    return datetime.utcnow() + timedelta(seconds=LOT_LIFE_TIME_SECONDS)


class Lot(Base):
    __tablename__ = "lot"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(32))
    description: Mapped[str] = mapped_column(String(128))
    starting_price: Mapped[Decimal]
    end_time: Mapped[datetime] = mapped_column(default=lot_end_time)
    bids: Mapped[list["Bid"]] = relationship(
        "Bid",
        back_populates="lot",
        cascade="all, delete-orphan",
        primaryjoin="Lot.id == Bid.lot_id",
        lazy="selectin",
    )

    def __repr__(self):
        return (
            f"Lot({self.id=}, "
            f"{self.title=}, "
            f"{self.description=}, "
            f"{self.starting_price=}, "
            f"{self.end_time=})"
        )

    @hybrid_property
    def is_ended(self):
        return datetime.utcnow() > self.end_time


class Bid(Base):
    __tablename__ = "bid"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[Decimal]

    lot_id: Mapped[int] = mapped_column(ForeignKey("lot.id"))
    lot: Mapped["Lot"] = relationship("Lot", back_populates="bids")

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user = relationship("User", back_populates="bids")

    def __repr__(self):
        return f"Bid({self.id=}, {self.amount=})"
