from fastapi import Depends

from app.lots.repositories import LotRepository
from app.lots.schemas import Lot
from app.lots.services import LotService


def lot_service() -> LotService[Lot]:
    return LotService[Lot](LotRepository())


ActiveLotService = Depends(lot_service)
