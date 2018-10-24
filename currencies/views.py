from django.views.generic import ListView, CreateView

from .forms import CurrencyRateForm
from .models import CurrencyRate


class CurrencyOnlineView(ListView):
    queryset = CurrencyRate.objects.all()


class CurrencyListView(ListView):
    queryset = CurrencyRate.objects.all()


class CurrencyRateListView(ListView):
    queryset = CurrencyRate.objects.all()


class CurrencyCreateView(CreateView):
    form_class = CurrencyRateForm
    queryset = CurrencyRate.objects.all()
    success_url = '/currencies/rate/'
