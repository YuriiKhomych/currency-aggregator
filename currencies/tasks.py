import logging
import requests
import json
from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer

from .models import CurrencyRate

channel_layer = get_channel_layer()
logger = logging.getLogger()


@shared_task
def get_currencies():
    rates = CurrencyRate.objects.all()
    for rate in rates:
        res = requests.get(
            f"https://api.cryptonator.com/api/ticker/{rate.base.lower()}-{rate.target.lower()}"
        ).json()
        price = res['ticker']['price']
        logger.info(price)
        logger.info(f'Update rate for {rate.base}-{rate.target}: {rate.price}')
        rate.update_currency_rate(price)
