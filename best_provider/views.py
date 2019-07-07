from django.shortcuts import render
from best_provider.ExchangeRateManager import ExchangeRateManager


def home_page(request):
    currency_manager = ExchangeRateManager()
    provider = currency_manager.get_best_provider()

    currencies = {}
    if provider:
        currencies = currency_manager.get_all(provider)

    return render(request, 'home.html', {'currencies': currencies, 'provider': provider})
