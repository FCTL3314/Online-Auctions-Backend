from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.base.repositories import AbstractRepository, AbstractCreateRepository
from app.lots.models import Lot
from app.lots.schemas import LotCreate


class LotRepository(AbstractCreateRepository, AbstractRepository):
    async def one(self, lot_id: int, session: AsyncSession) -> Lot | None:
        stmt = select(Lot).where(Lot.id == lot_id)
        result = await session.execute(stmt)
        return result.scalars().first()

    async def all(self, session: AsyncSession) -> Sequence[Lot]:
        stmt = select(Lot)
        result = await session.execute(stmt)
        return result.scalars().all()

    async def create(self, lot: LotCreate, session: AsyncSession) -> Lot:
        new_lot = Lot(
            title=lot.title,
            description=lot.description,
            starting_price=lot.starting_price,
            end_time=lot.end_time,
        )
        session.add(new_lot)
        await session.commit()
        await session.refresh(new_lot)
        return new_lot
