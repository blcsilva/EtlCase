from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Função para extração
def extract():
    df = pd.read_csv('/opt/airflow/data/sales_data.csv')
    df.to_csv('/opt/airflow/data/extracted_data.csv', index=False)
    print("Dados extraídos com sucesso")

# Função para transformação
def transform():
    df = pd.read_csv('/opt/airflow/data/extracted_data.csv')
    df['Sales'] = df['Sales'] * 1.1  # Exemplo: adicionar 10% às vendas
    df.to_csv('/opt/airflow/data/transformed_data.csv', index=False)
    print("Dados transformados com sucesso")

# Função para carga
def load():
    # Conexão com o banco de dados PostgreSQL
    conn_str = "postgresql://username:password@postgres_host:postgres_port/db_name"
    engine = create_engine(conn_str)

    df = pd.read_csv('/opt/airflow/data/transformed_data.csv')
    
    # Carregar os dados no PostgreSQL
    df.to_sql('sales', engine, if_exists='replace', index=False)
    print("Dados carregados com sucesso")

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1
}

with DAG(dag_id='etl_sales_data',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load
    )

    extract_task >> transform_task >> load_task
