from django.test import TestCase
from optimal_provider.models import Provider


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class ProviderTest(TestCase):

    def test_saving_and_retrieving_providers(self):
        first_provider = Provider()
        first_provider.url = 'http://mock.io/232323'

        first_provider.save()

        self.assertEqual(first_provider.url, 'http://mock.io/232323')
