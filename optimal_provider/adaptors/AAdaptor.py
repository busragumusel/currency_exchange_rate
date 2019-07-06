from optimal_provider.adaptors.AbstractAdaptor import AbstractAdaptor
from optimal_provider.adaptors.providers.AProvider import AProvider


class AAdaptor(AbstractAdaptor):

    def __init__(self):
        self.provider = AProvider()

    def all(self):
        return self.provider.get()

    def provider_name(self):
        return 'aProvider'
