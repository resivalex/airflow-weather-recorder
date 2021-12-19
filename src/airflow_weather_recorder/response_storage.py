from clickhouse_driver import Client
from .config import clickhouse_host, clickhouse_port, clickhouse_database, clickhouse_user, clickhouse_password
import datetime


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
