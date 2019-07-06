from django.shortcuts import render
from optimal_provider.CurrencyManager import CurrencyManager


def home_page(request):
    currency_manager = CurrencyManager()
    provider = currency_manager.get_optimal_provider()

    currencies = {}
    if provider:
        currencies = currency_manager.get_all(provider)

    return render(request, 'home.html', {'currencies': currencies, 'provider': provider})
