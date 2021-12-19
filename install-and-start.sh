#!/bin/bash

pip install poetry
poetry config virtualenvs.in-project true
poetry install
AIRFLOW_HOME='.' poetry run airflow standalone

echo "\nWait for Ctrl-C"
trap 'kill $(jobs -p)' INT
sleep infinity &
wait
