class GetRateList:
    def __init__(self, adaptor):
        self._strategy = adaptor

    def all(self):
        return self._strategy.all()
