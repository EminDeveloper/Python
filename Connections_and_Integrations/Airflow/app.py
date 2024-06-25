from airflow import DAG

from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'Dumbulu',
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
        dag_id='our_first_dag',
        default_args=default_args,
        description='This is your first Airflw dag',
        start_date=datetime(2024, 6, 25, 11),
        schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='task_000001',
        bash_command='Echo Hello World, this is my first Dag and task',
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo hey, I am task2 and will be running after task1!"
    )

    task3 = BashOperator(
        task_id='thrid_task',
        bash_command="echo hey, I am task3 and will be running after task1 at the same time as task2!"
    )

    # Task dependency method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # Task dependency method 2
    # task1 >> task2
    # task1 >> task3

    # Task dependency method 3
    task1 >> [task2, task3]

