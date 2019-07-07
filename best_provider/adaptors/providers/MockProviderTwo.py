import requests


class MockProviderTwo:

    def get_all(self):
        return requests.get('http://www.mocky.io/v2/5d19ec932f00004e00fd7326').json()
