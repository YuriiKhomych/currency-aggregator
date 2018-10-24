from django.views.generic import ListView, CreateView

from .forms import CurrencyRateForm
from .models import CurrencyRate


class CurrencyOnlineView(ListView):
    template_name = 'currencies/currency_online.html'
    queryset = CurrencyRate.objects.all()


class CurrencyListView(ListView):
    template_name = 'currencies/currency_list.html'
    queryset = CurrencyRate.objects.all()


class CurrencyRateListView(ListView):
    template_name = 'currencies/currency_rate_list.html'
    queryset = CurrencyRate.objects.all()


class CurrencyCreateView(CreateView):
    template_name = 'currencies/new_currency.html'
    form_class = CurrencyRateForm
    queryset = CurrencyRate.objects.all()
    success_url = '/currencies/rate/'
