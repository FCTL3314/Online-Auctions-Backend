from decimal import Decimal
from typing import Generic

from fastapi import HTTPException
from fastapi_pagination import paginate, Page
from sqlalchemy.ext.asyncio import AsyncSession

from app.base.services import (
    AbstractRetrieveService,
    AbstractListService,
    AbstractCreateService,
    T,
    REPO_T,
)
from app.lots.constants import LOT_NOT_FOUND_MESSAGE, MIN_NEW_BID_PERCENT
from app.lots.filters import LotFilter
from app.lots.models import Lot
from app.lots.repositories import LotRepository
from app.utils import is_obj_exists_or_404


class LotService(
    AbstractRetrieveService,
    AbstractListService,
    AbstractCreateService,
    Generic[T, REPO_T],
):
    async def retrieve(self, lot_id: int, session: AsyncSession) -> T:
        lot = await self.repository.get(lot_id, session)
        is_obj_exists_or_404(lot, LOT_NOT_FOUND_MESSAGE)
        return lot

    async def list(self, lot_filer: LotFilter, session: AsyncSession) -> Page[T]:
        return paginate(await self.repository.all(lot_filer, session))

    async def create(self, lot: T, session: AsyncSession) -> T:
        return await self.repository.create(lot, session)


class BidService(AbstractCreateService, Generic[T, REPO_T]):
    lot_repository = LotRepository()

    async def create(self, lot_id: int, bid: T, session: AsyncSession) -> T:
        lot = await self.lot_repository.get(lot_id, session)
        is_obj_exists_or_404(lot, LOT_NOT_FOUND_MESSAGE)
        self.validate_bid_more_than_lot_starting_price(bid, lot)
        await self.validate_bid_more_than_current_max_bid(lot_id, bid, session)
        return await self.repository.create(lot_id, bid, session)

    @staticmethod
    def validate_bid_more_than_lot_starting_price(bid: T, lot: Lot) -> None:
        if bid.amount <= lot.starting_price:
            raise HTTPException(
                detail=f"The bid amount should be greater then lot starting price.",
                status_code=400,
            )

    async def validate_bid_more_than_current_max_bid(
        self, lot_id: int, bid: T, session: AsyncSession
    ) -> None:
        max_bid = await self.repository.max_bid(lot_id, session)
        if max_bid is not None and bid.amount <= max_bid.amount * Decimal(
            MIN_NEW_BID_PERCENT
        ):
            raise HTTPException(
                detail=f"The bid amount must be 5 percent more than the current maximum bid.",
                status_code=400,
            )
