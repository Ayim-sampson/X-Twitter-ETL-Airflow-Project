from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from x_etl import run_x_etl


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 2, 5),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}   

dag = DAG(
    'x_dag',
    default_args=default_args,
    description='My First etl code'
)

run_etl = PythonOperator(
    task_id='complete_x_etl',
    python_callable=run_x_etl,
    dag=dag,
)