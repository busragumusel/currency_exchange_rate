from abc import abstractmethod, ABCMeta


class AbstractAdaptor(metaclass=ABCMeta):

    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def provider_name(self):
        pass
