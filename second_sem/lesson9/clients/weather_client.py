import requests


class WeatherClient:

    BASE_URL = 'https://api.openweathermap.org/data/2.5/'

    def __init__(self, token):
        self.token = token
        self.weather_prefix = 'weather'

    def get_temp_by_city_name(self, city_name):
        """Получаем погоду по наименованию города"""
        url = f'{self.BASE_URL}/{self.weather_prefix}'
        params = {
            "q": city_name,
            "appid": self.token,
            "units": "metric",
            "lang": "ru",
        }
        return requests.get(url, params).json()
