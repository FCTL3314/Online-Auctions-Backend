from fastapi import Depends
from fastapi_filter import FilterDepends

from app.lots.filters import LotFilter
from app.lots.repositories import LotRepository, BidRepository
from app.lots.models import Lot, Bid
from app.lots.services import LotService, BidService


def get_lot_service() -> LotService[Lot, LotRepository]:
    return LotService[Lot, LotRepository](LotRepository())


ActiveLotService = Depends(get_lot_service)
ActiveLotFilter = FilterDepends(LotFilter)


def get_bid_service() -> BidService[Bid, BidRepository]:
    return BidService[Bid, BidRepository](BidRepository())


ActiveBidService = Depends(get_bid_service)
