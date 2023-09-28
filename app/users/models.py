from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32))

    def __repr__(self):
        return (
            f"User(id={self.id}, "
            f"name={self.name}, "
            f"email={self.email}, "
            f"hashed_password={self.hashed_password}, "
            f"is_active={self.is_active}, "
            f"is_superuser={self.is_superuser}, "
            f"is_verified={self.is_verified})"
        )
