from django.urls import path
from .views import CurrencyCreateView, CurrencyOnlineView, CurrencyListView, CurrencyRateListView

app_name = 'currencies'
urlpatterns = [
    path('online', CurrencyOnlineView.as_view(), name='currencies-online'),
    path('create', CurrencyCreateView.as_view(), name='currencies-create'),
    path('', CurrencyListView.as_view(), name='currencies-list'),
    path('rates/', CurrencyRateListView.as_view(), name='currencies-rates-list'),
]
