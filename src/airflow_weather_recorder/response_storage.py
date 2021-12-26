from clickhouse_driver import Client
from .config import clickhouse_host, clickhouse_port, clickhouse_database, clickhouse_user, clickhouse_password
import datetime
import json


CELSIUS_ABSOLUTE_ZERO = -273.15


def save_record(response: str):
    client = Client(
        host=clickhouse_host,
        port=clickhouse_port,
        database=clickhouse_database,
        user=clickhouse_user,
        password=clickhouse_password
    )
    client.execute('''
        INSERT INTO weather_requests
        (datetime, response)
        VALUES
    ''', [[datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S"), response]])
    info = json.loads(response)
    record = [
        info['dt'],
        ', '.join([weather['main'] for weather in info['weather']]),
        info['main']['temp'] + CELSIUS_ABSOLUTE_ZERO,
        info['main']['feels_like'] + CELSIUS_ABSOLUTE_ZERO,
        info['wind']['speed']
    ]
    client.execute('''
        INSERT INTO weather_log
        (timestamp, weather_name, temperature, feels_like_temperature, wind_speed)
        VALUES
    ''', [record])
