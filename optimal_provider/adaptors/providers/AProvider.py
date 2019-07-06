import requests


class AProvider:

    def get(self):
        return requests.get('http://www.mocky.io/v2/5d19ec692f00002c00fd7324').json()
