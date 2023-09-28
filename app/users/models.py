from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(128))

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email}, password={self.password})"
