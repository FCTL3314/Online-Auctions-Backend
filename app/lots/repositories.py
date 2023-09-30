from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.base.repositories import (
    AbstractCreateRepository,
    AbstractGetRepository,
    AbstractAllRepository,
)
from app.lots.constants import LOT_ORDER_FIELDS
from app.lots.filters import LotFilter
from app.lots.models import Lot, Bid
from app.lots.schemas import LotCreate, Bid as BidSchema
from app.users.models import User
from app.users.schemas import UserRead


class LotRepository(
    AbstractGetRepository, AbstractAllRepository, AbstractCreateRepository
):
    base_query = select(Lot)

    async def get(self, lot_id: int, session: AsyncSession) -> Lot | None:
        query = self.base_query.where(Lot.id == lot_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()

    async def all(self, lot_filter: LotFilter, session: AsyncSession) -> Sequence[Lot]:
        query = self.base_query.order_by(*LOT_ORDER_FIELDS)
        filtered_stmt = lot_filter.filter(query)
        result = await session.execute(filtered_stmt)
        return result.scalars().all()

    async def create(self, lot: LotCreate, session: AsyncSession) -> Lot:
        new_lot = Lot(
            title=lot.title,
            description=lot.description,
            starting_price=lot.starting_price,
        )
        session.add(new_lot)
        await session.commit()
        await session.refresh(new_lot)
        return new_lot


class BidRepository(AbstractCreateRepository):
    base_query = select(Bid)

    async def winning_bids(self, session: AsyncSession) -> Sequence[Bid]:
        query = (
            self.base_query
            .join(Lot, Bid.lot_id == Lot.id)
            .where(Lot.is_ended.is_(True))  # noqa
            .order_by(Bid.lot_id.desc(), Bid.amount.desc())
            .distinct(Bid.lot_id)
        )
        result = await session.execute(query)
        return result.scalars().all()

    async def max_bid(self, lot_id: int, session: AsyncSession) -> Bid | None:
        query = self.base_query.where(Lot.id == lot_id).order_by(Bid.amount.desc())
        result = await session.execute(query)
        return result.scalars().first()

    async def create(
        self, lot_id: int, bid: BidSchema, user: UserRead, session: AsyncSession
    ) -> Bid:
        bid = Bid(amount=bid.amount, lot_id=lot_id, user_id=user.id)
        session.add(bid)
        await session.commit()
        await session.refresh(bid)
        return bid
