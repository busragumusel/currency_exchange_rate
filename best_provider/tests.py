from django.test import TestCase
from best_provider.models import ExchangeRate
from best_provider.ExchangeRateManager import ExchangeRateManager
from django.core.management import call_command


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class CurrencyTest(TestCase):

    def test_saving_and_retrieving_exchange_rate(self):
        exchange_rate = ExchangeRate()
        exchange_rate.provider = 'http://mock.io/232323',
        exchange_rate.rate = 4.14234
        exchange_rate.code = 'usd'
        exchange_rate.save()

        saved_exchange_rate = ExchangeRate.objects.all()

        self.assertEqual(saved_exchange_rate.count(), 1)


class CommandsTestCase(TestCase):

    def test_my_command(self):
        """Add rates to db"""

        args = []
        opts = {}
        call_command('add_rates_to_db', *args, **opts)

        self.assertGreater(ExchangeRate.objects.all().count(), 0)


class ExchangeRateTest(TestCase):

    def test_find_best_provider(self):
        exchange_rate = ExchangeRate()
        exchange_rate.provider = 'http://www.mocky.io/v2/5d19ec932f00004e00fd7326'
        exchange_rate.code = 'usd'
        exchange_rate.rate = 4.14234
        exchange_rate.save()

        exchange_rate2 = ExchangeRate()
        exchange_rate2.provider = 'http://www.mocky.io/v2/5d19ec932f00004e00fd7326'
        exchange_rate2.code = 'eur'
        exchange_rate2.rate = 4.68234
        exchange_rate2.save()

        exchange_rate3 = ExchangeRate()
        exchange_rate3.provider = 'http://www.mocky.io/v2/5d19ec932f00004e00fd7326'
        exchange_rate3.code = 'gbp'
        exchange_rate3.rate = 5.01234
        exchange_rate3.save()

        exchange_rate4 = ExchangeRate()
        exchange_rate4.provider = 'http://www.mocky.io/v2/5d19ec932f00004e00fd7326'
        exchange_rate4.code = 'usd'
        exchange_rate4.rate = 4.14234
        exchange_rate4.save()

        exchange_rate5 = ExchangeRate()
        exchange_rate5.provider = 'http://www.mocky.io/v2/5d19ec692f00002c00fd7324'
        exchange_rate5.code = 'eur'
        exchange_rate5.rate = 4.67234
        exchange_rate5.save()

        exchange_rate6 = ExchangeRate()
        exchange_rate6.provider = 'http://www.mocky.io/v2/5d19ec692f00002c00fd7324'
        exchange_rate6.code = 'gbp'
        exchange_rate6.rate = 5.01034
        exchange_rate6.save()

        exchange_rate_manager = ExchangeRateManager()
        self.assertEqual(exchange_rate_manager.get_best_provider()['provider'],
                         'http://www.mocky.io/v2/5d19ec932f00004e00fd7326')

    def test_get_exchange_rates_from_provider(self):
        args = []
        opts = {}
        call_command('add_rates_to_db', *args, **opts)

        provider = {
            'provider': 'http://www.mocky.io/v2/5d19ec932f00004e00fd7326'
        }

        exchange_rate_manager = ExchangeRateManager()
        self.assertEqual((list(exchange_rate_manager.get_all(provider).values('code', 'rate'))), [
            {
                "code": "usd",
                "rate": 4.14234
            },
            {
                "code": "eur",
                "rate": 4.68234
            },
            {
                "code": "gbp",
                "rate": 5.01234
            }
        ])