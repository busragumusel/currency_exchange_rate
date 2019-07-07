from django.db.models import Sum
from optimal_provider.models import ExchangeRate


class ExchangeRateManager:

    def get_optimal_provider(self):
        return ExchangeRate.objects.values('provider').annotate(sum=Sum('rate')).order_by('-sum').first()

    def get_all(self, provider):
        return ExchangeRate.objects.filter(provider=provider['provider'])
