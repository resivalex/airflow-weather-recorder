from .config import open_weather_api_key
import requests


def get_city_wheather(city):
    return f'Good weather in {city}!'
    return requests.get(
        'https://api.openweathermap.org/data/2.5/weather',
        params=dict(city=city, appid=open_weather_api_key)
    )
