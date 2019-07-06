from django.db.models import Sum
from optimal_provider.models import Currencies


class CurrencyManager:

    def get_optimal_provider(self):
        return Currencies.objects.values('provider').annotate(sum=Sum('rate')).order_by('-sum').first()

    def get_all(self, provider):
        return Currencies.objects.filter(provider=provider['provider'])
