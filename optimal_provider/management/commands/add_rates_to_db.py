from django.core.management.base import BaseCommand
from optimal_provider.adaptors.AAdaptor import AAdaptor
from optimal_provider.adaptors.BAdaptor import BAdaptor
from optimal_provider.adaptors.strategy.GetRateList import GetRateList
from optimal_provider.models import Currencies


class Command(BaseCommand):
    """This command triggers exchane update process"""

    def handle(self, *args, **options):
        """Handle command"""

        adaptors = [
            AAdaptor,
            BAdaptor
        ]

        for adaptor in adaptors:
            adaptor_instance = adaptor()
            provider_url = adaptor_instance.provider_url()
            data = GetRateList(adaptor_instance).all()

            for currency in data:
                Currencies.objects.create(provider=provider_url, code=currency['code'], rate=currency['rate'])
