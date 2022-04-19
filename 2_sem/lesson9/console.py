import argparse
from datetime import datetime

from clients.weather_client import WeatherClient
from clients.currency_client import CurrencyClient


def get_temp_by_city(city_name):
    current_time = datetime.now()
    w_client = WeatherClient("**")
    response = w_client.get_temp_by_city_name(city_name)
    if response["cod"] == 200:
        result_str = (
            f"Сейчас {current_time}\n"
            f"В городе {response['name']} сейчас {response['weather'][0]['description']}. \n"
            f"На улице {response['main']['temp']} градусов, "
            f"ощущается как {response['main']['feels_like']}. \n"
            f"Скорость ветра: {response['wind']['speed']} м/с. \n"
            f"Влажность: {response['main']['humidity']}% \n"
        )
    elif response["cod"] == "404":
        result_str = "Город не найден"
    else:
        result_str = response['message']

    return result_str


def get_currency():
    current_time = datetime.now()
    c_client = CurrencyClient()
    response = c_client.get_latest_currency()
    result_str = (
        f"Сейчас {current_time}\n"
        f"USD/RUB: {response['rates']['RUB']}\n"
    )
    return result_str


if __name__=='__main__':
    parser = argparse.ArgumentParser(
        description='My console'
    )
    parser.add_argument(
        '--mode',
        dest='mode',
        type=str,
        help='Вариант запуска',
    )
    parser.add_argument(
        '--city',
        dest='city',
        type=str,
        help='Наименование города',
        default='',
        required=False,
    )

    args = parser.parse_args()

    if args.mode == 'weather':
        print(get_temp_by_city(args.city))
    elif args.mode == "currency":
        print(get_currency())
