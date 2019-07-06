from optimal_provider.adaptors.AbstractAdaptor import AbstractAdaptor
from optimal_provider.adaptors.providers.MockProviderOne import MockProviderOne


class MockProviderOneAdaptor(AbstractAdaptor):

    def __init__(self):
        self.provider = MockProviderOne()

    def all(self):
        return self.provider.get()

    def provider_url(self):
        return 'http://www.mocky.io/v2/5d19ec932f00004e00fd7326'
