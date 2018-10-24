from django import forms

from .models import CurrencyRate


class CurrencyRateForm(forms.ModelForm):
    class Meta:
        model = CurrencyRate
        fields = ('base', 'target',)
