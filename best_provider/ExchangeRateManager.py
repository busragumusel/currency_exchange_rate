from django.db.models import Sum
from best_provider.models import ExchangeRate


class ExchangeRateManager:

    def get_best_provider(self):
        return ExchangeRate.objects.values('provider').annotate(sum=Sum('rate')).order_by('-sum').first()

    def get_all(self, provider):
        return ExchangeRate.objects.filter(provider=provider['provider'])
