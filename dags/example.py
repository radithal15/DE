from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
import datetime

with DAG(
    dag_id="example",
    start_date=datetime.datetime(2021, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["example"],
) as dag:
    dag.doc_md = __doc__

    print_hello_world = BashOperator(
        task_id="print_hello_world",
        bash_command="echo 'hello world'",
    )

    def hello_world():
        return "hello world from python"

    print_hello_world = PythonOperator(
        task_id="print_hello_world_python",
        python_callable=hello_world,
    )

    print_hello_world