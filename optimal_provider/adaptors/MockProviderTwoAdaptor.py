from optimal_provider.adaptors.AbstractAdaptor import AbstractAdaptor
from optimal_provider.adaptors.providers.MockProviderTwo import MockProviderTwo


class MockProviderTwoAdaptor(AbstractAdaptor):

    def __init__(self):
        self.provider = MockProviderTwo()

    def all(self):
        return self.provider.get_all()

    def provider_url(self):
        return 'http://www.mocky.io/v2/5d19ec692f00002c00fd7324'


