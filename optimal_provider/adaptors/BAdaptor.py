from optimal_provider.adaptors.AbstractAdaptor import AbstractAdaptor
from optimal_provider.adaptors.providers.BProvider import BProvider


class BAdaptor(AbstractAdaptor):

    def __init__(self):
        self.provider = BProvider()

    def all(self):
        return self.provider.get_all()

    def provider_url(self):
        return 'http://www.mocky.io/v2/5d19ec932f00004e00fd7326'


