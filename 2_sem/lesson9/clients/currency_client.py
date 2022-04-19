import requests


class CurrencyClient:

    BASE_URL = 'https://cdn.cur.su/api/'

    def __init__(self):
        self.latest_prefix = 'latest.json'

    def get_latest_currency(self):
        """Получаем погоду по наименованию города"""
        url = f'{self.BASE_URL}/{self.latest_prefix}'
        return requests.get(url).json()
