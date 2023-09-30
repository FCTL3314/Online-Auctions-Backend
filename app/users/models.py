from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(primary_key=True)  # type: ignore[assignment]
    name: Mapped[str] = mapped_column(String(32))

    def __repr__(self):
        return (
            f"User({self.id=}, "
            f"{self.name=}, "
            f"{self.email=}, "
            f"{self.hashed_password=}, "
            f"{self.is_active=}, "
            f"{self.is_superuser=}, "
            f"{self.is_verified=})"
        )
