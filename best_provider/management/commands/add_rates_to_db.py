from django.core.management.base import BaseCommand
from best_provider.adaptors.MockProviderOneAdaptor import MockProviderOneAdaptor
from best_provider.adaptors.MockProviderTwoAdaptor import MockProviderTwoAdaptor
from best_provider.adaptors.strategy.GetRateList import GetRateList
from best_provider.models import ExchangeRate


class Command(BaseCommand):
    """This command triggers exchane update process"""

    def handle(self, *args, **options):
        """Handle command"""

        adaptors = [
            MockProviderOneAdaptor,
            MockProviderTwoAdaptor
        ]

        for adaptor in adaptors:
            adaptor_instance = adaptor()
            provider_url = adaptor_instance.provider_url()
            data = GetRateList(adaptor_instance).all()

            if ExchangeRate.objects.filter(provider=provider_url).count() == 0:
                for currency in data:
                    ExchangeRate.objects.create(provider=provider_url, code=currency['code'], rate=currency['rate'])
