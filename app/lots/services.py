from typing import TypeVar, Generic

from fastapi_pagination import paginate, Page
from sqlalchemy.ext.asyncio import AsyncSession

from app.base.services import (
    AbstractRetrieveService,
    AbstractListService,
    AbstractCreateService,
)
from app.lots.constants import LOT_NOT_FOUND_MESSAGE
from app.lots.filters import LotFilter
from app.utils import is_obj_exists_or_404

T = TypeVar("T")


class LotService(
    AbstractRetrieveService, AbstractListService, AbstractCreateService, Generic[T]
):
    async def retrieve(self, lot_id: int, session: AsyncSession) -> T:
        lot = await self.repository.one(lot_id, session)
        is_obj_exists_or_404(lot, LOT_NOT_FOUND_MESSAGE)
        return lot

    async def list(self, lot_filer: LotFilter, session: AsyncSession) -> Page[T]:
        return paginate(await self.repository.all(lot_filer, session))

    async def create(self, lot: T, session: AsyncSession) -> T:
        return await self.repository.create(lot, session)
