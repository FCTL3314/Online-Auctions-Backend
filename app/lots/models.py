from datetime import datetime, timedelta
from decimal import Decimal

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.bids.models import Bid
from app.db import Base
from app.lots.constants import LOT_LIFE_TIME_SECONDS


def lot_end_time() -> datetime:
    return datetime.now() + timedelta(seconds=LOT_LIFE_TIME_SECONDS)


class Lot(Base):
    __tablename__ = "lot"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(32))
    description: Mapped[str] = mapped_column(String(128))
    starting_price: Mapped[Decimal]
    end_time: Mapped[datetime] = mapped_column(default=lot_end_time)
    bids: Mapped[list[Bid]] = relationship(
        Bid,
        back_populates="lot",
        cascade="all, delete-orphan",
        primaryjoin="Lot.id == Bid.lot_id",
        lazy="selectin",
    )

    def __repr__(self):
        return (
            f"Lot("
            f"id={self.id}, "
            f"title={self.title}, "
            f"description={self.description}, "
            f"starting_price={self.starting_price}, "
            f"end_time={self.end_time})"
        )
