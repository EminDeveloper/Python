from airflow import DAG
from datetime import datetime
from airflow.operators.python import (
    PythonOperator
)


def message():
    print("You create first dag in Apache Airflow. Nice to meet you!")


with DAG(dag_id="FirstDAG", start_date=datetime(2024, 6, 27), schedule_interval="@hourly",
         catchup=False) as dag:
    task = PythonOperator(
        task_id="task",
        python_callable=message
    )

task
