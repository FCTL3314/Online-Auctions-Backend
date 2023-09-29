from datetime import datetime, timedelta
from typing import TypeVar, Generic

from sqlalchemy.ext.asyncio import AsyncSession

from app.base.services import (
    AbstractRetrieveService,
    AbstractListService,
    AbstractCreateService,
)
from app.lots.constants import LOT_NOT_FOUND_MESSAGE, LOT_LIFE_TIME_SECONDS
from app.utils import is_obj_exists_or_404

T = TypeVar("T")


class LotService(
    AbstractRetrieveService, AbstractListService, AbstractCreateService, Generic[T]
):
    async def retrieve(self, lot_id: int, session: AsyncSession) -> T:
        lot = await self.repository.one(lot_id, session)
        is_obj_exists_or_404(lot, LOT_NOT_FOUND_MESSAGE)
        return lot

    async def list(self, session: AsyncSession) -> list[T]:
        return await self.repository.all(session)

    async def create(self, lot: T, session: AsyncSession) -> T:
        return await self.repository.create(lot, session)


def lot_end_time() -> datetime:
    return datetime.now() + timedelta(seconds=LOT_LIFE_TIME_SECONDS)
