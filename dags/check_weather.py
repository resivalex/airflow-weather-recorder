from datetime import datetime
from pprint import pprint
from airflow_weather_recorder.weather import get_city_wheather

from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG(
    dag_id='weather_python_operator',
    schedule_interval='* * * * *',
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['weather'],
) as dag:

    def check_weather():
        weather_info = get_city_wheather('Yaroslavl')
        pprint(weather_info)

    root = PythonOperator(
        task_id='check_weather',
        python_callable=check_weather,
    )
