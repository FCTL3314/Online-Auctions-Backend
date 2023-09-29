from fastapi import APIRouter
from fastapi_pagination import Page
from sqlalchemy.ext.asyncio import AsyncSession

from app.lots.constants import LOT_TAG
from app.lots.dependencies import LotService, ActiveLotService, ActiveLotFilter
from app.lots.filters import LotFilter
from app.lots.schemas import Lot, LotWithBids, LotCreate
from dependencies import ActiveSession

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
