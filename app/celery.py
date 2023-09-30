from datetime import timedelta

from celery import Celery

from app.config import config

celery = Celery(
    __name__,
    include=["app.lots.tasks"],
)

celery.conf.broker_url = config.rabbitmq_amqp_url
celery.conf.result_backend = config.rabbitmq_rpc_url
celery.conf.beat_schedule = {
    "auction_winner_determination": {
        "task": "app.lots.tasks.determinate_auction_winner",
        "schedule": timedelta(minutes=1),
    },
}
