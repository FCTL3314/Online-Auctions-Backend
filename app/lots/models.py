from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Lot(Base):
    __tablename__ = "lot"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(32))
    description: Mapped[str] = mapped_column(String(128))
    starting_price: Mapped[float]
    end_time: Mapped[datetime]

    def __repr__(self):
        return (
            f"Lot("
            f"id={self.id}, "
            f"title={self.title}, "
            f"description={self.description}, "
            f"starting_price={self.starting_price}, "
            f"end_time={self.end_time})"
        )
