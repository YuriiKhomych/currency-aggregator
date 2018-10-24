from django.db import models


class CurrencyRate(models.Model):
    base = models.CharField(max_length=10)
    target = models.CharField(max_length=10)
    price = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.base}-{self.target}-{self.price}'

    def update_currency_rate(self, price):
        if self.price != price:
            self.price = price
            self.save()
