from optimal_provider.adaptors.AbstractAdaptor import AbstractAdaptor
from optimal_provider.adaptors.providers.BProvider import BProvider


class BAdaptor(AbstractAdaptor):

    def __init__(self):
        self.provider = BProvider()

    def all(self):
        return self.provider.get_all()

    def provider_name(self):
        return 'bProvider'


