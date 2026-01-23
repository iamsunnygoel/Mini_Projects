airflow_livetest

from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'coder2',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='sunnytest_v3',
    description='A simple test DAG for sunny weather conditions',
    schedule_interval='@daily',
    start_date=datetime(2025, 7, 25),
) as dag:
    task1 = BashOperator(
        task_id='print_sunny_message',
        bash_command='echo "Day1,It is a sunny day!"')
    
    task2 = BashOperator(
        task_id='print_sunny2_advice',
        bash_command='echo "Day2,Remember to wear sunscreen!"')
    
    task3 = BashOperator(
        task_id='print_sunny3_advice',
        bash_command='echo "Day3,Stay hydrated and enjoy the sunshine!"')

    task1 >> task2
    task1 >> task3