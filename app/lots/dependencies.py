from fastapi import Depends
from fastapi_filter import FilterDepends

from app.lots.filters import LotFilter
from app.lots.repositories import LotRepository
from app.lots.schemas import Lot
from app.lots.services import LotService


def lot_service() -> LotService[Lot]:
    return LotService[Lot](LotRepository())


ActiveLotService = Depends(lot_service)
ActiveLotFilter = FilterDepends(LotFilter)
