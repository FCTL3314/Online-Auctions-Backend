from fastapi import APIRouter
from fastapi_pagination import Page
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import ActiveSession
from app.lots.constants import BID_TAG
from app.lots.constants import LOT_TAG
from app.lots.dependencies import (
    LotService,
    ActiveLotService,
    ActiveLotFilter,
    ActiveBidService,
)
from app.lots.filters import LotFilter
from app.lots.schemas import Lot, LotWithBids, LotCreate, Bid, BidCreate
from app.lots.services import BidService
from app.users.dependencies import ActiveUser
from app.users.schemas import UserRead

router = APIRouter()


@router.get(
    "/{lot_id}/",
    name="lot:retrieve",
    response_model=LotWithBids,
    description="Get lot details by id.",
    tags=[LOT_TAG],
)
async def lot_retrieve(
    lot_id: int,
    lot_service: LotService = ActiveLotService,
    session: AsyncSession = ActiveSession,
) -> LotWithBids:
    return await lot_service.retrieve(lot_id, session)


@router.get(
    "/",
    name="lot:list",
    response_model=Page[Lot],
    description="Get a list of all lots.",
    tags=[LOT_TAG],
)
async def lot_list(
    lot_service: LotService = ActiveLotService,
    lot_filter: LotFilter = ActiveLotFilter,
    session: AsyncSession = ActiveSession,
) -> Page[Lot]:
    return await lot_service.list(lot_filter, session)


@router.post(
    "/",
    name="lot:create",
    response_model=Lot,
    description="Creates a new lot.",
    tags=[LOT_TAG],
)
async def lot_create(
    lot: LotCreate,
    lot_service: LotService = ActiveLotService,
    session: AsyncSession = ActiveSession,
) -> Lot:
    return await lot_service.create(lot, session)


@router.post(
    "/{lot_id}/bids",
    name="bid:create",
    response_model=Bid,
    description="Creates a new bid.",
    tags=[BID_TAG],
)
async def bid_create(
    lot_id: int,
    bid: BidCreate,
    user: UserRead = ActiveUser,
    bid_service: BidService = ActiveBidService,
    session: AsyncSession = ActiveSession,
) -> Bid:
    return await bid_service.create(lot_id, bid, user, session)
