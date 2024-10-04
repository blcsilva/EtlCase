from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

# Funções de exemplo para as etapas do ETL
def extract(**kwargs):
    # Código de extração de dados
    pass

def transform(**kwargs):
    # Código de transformação de dados
    pass

def load(**kwargs):
    # Código de carga de dados
    pass

# Definição da DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'etl_example',
    default_args=default_args,
    description='ETL example DAG',
    schedule_interval=timedelta(days=1),
)

# Definição das tarefas (tasks)
t1 = PythonOperator(
    task_id='extract',
    python_callable=extract,
    dag=dag,
)

t2 = PythonOperator(
    task_id='transform',
    python_callable=transform,
    dag=dag,
)

t3 = PythonOperator(
    task_id='load',
    python_callable=load,
    dag=dag,
)

# Definindo a ordem das tarefas
t1 >> t2 >> t3
