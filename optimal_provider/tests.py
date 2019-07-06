from django.test import TestCase
from optimal_provider.models import Currencies


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class CurrencyTest(TestCase):

    def test_saving_and_retrieving_exchange_rate(self):
        exchange_rate = Currencies()
        exchange_rate.provider = 'http://mock.io/232323',
        exchange_rate.rate = 4.14234
        exchange_rate.code = 'usd'
        exchange_rate.save()

        saved_exchange_rate = Currencies.objects.all()

        self.assertEqual(saved_exchange_rate.count(), 1)
