from app.celery import celery
from app.db import scoped_session, scoped_loop
from app.lots.repositories import BidRepository
from app.lots.services import BidWinnerDeterminerService


def determinate_auction_winner_service():
    async with scoped_session() as session:
        BidWinnerDeterminerService(BidRepository()).execute(session)


@celery.task
def determinate_auction_winner():
    scoped_loop.run_until_complete(determinate_auction_winner_service())
