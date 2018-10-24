from django.urls import path
from .consumers import CurrenciesConsumer

websocket_urlpatterns = [
    path("ws/currencies/", CurrenciesConsumer)
]
