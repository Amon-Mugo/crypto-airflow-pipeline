from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'crypto_pipeline',
    default_args=default_args,
    description='Daily crypto dbt pipeline',
    schedule_interval='0 7 * * *',
    start_date=datetime(2026, 1, 1),
    catchup=False,
) as dag:

    run_dbt = BashOperator(
        task_id='run_dbt_models',
        bash_command='/home/amon/data_engineering/venv/bin/dbt run --project-dir /home/amon/data_engineering/crypto-analytics/crypto_dbt --profiles-dir /home/amon/.dbt ',
    )
