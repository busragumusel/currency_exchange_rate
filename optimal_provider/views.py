from django.db.models import Sum
from django.shortcuts import render
from optimal_provider.models import Currencies


def home_page(request):
    provider = Currencies.objects.values('provider').annotate(
        sum=Sum('rate')).order_by('-sum').first()

    currencies = {}
    if provider:
        currencies = Currencies.objects.filter(provider=provider['provider'])

    return render(request, 'home.html', {'currencies': currencies, 'provider': provider})
