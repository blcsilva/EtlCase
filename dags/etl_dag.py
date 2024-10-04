from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.base_hook import BaseHook
import pandas as pd
import mysql.connector
from datetime import datetime

def extract_data():
    # Conexão com o banco de dados MySQL
    conn = mysql.connector.connect(
        host='mysql',
        user='airflow',
        password='123456',
        database='airflow'
    )
    query = "SELECT * FROM your_source_table"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def transform_data(df):
    # Transforme os dados conforme necessário
    df['new_column'] = df['existing_column'] * 2  # Exemplo de transformação
    return df

def load_data(df):
    # Conexão com o banco de dados MySQL
    conn = mysql.connector.connect(
        host='mysql',
        user='airflow',
        password='123456',
        database='airflow'
    )
    df.to_sql('your_target_table', conn, if_exists='replace', index=False)
    conn.close()

with DAG(
    'etl_dag',
    default_args={'retries': 1},
    description='A simple ETL DAG',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    extract = PythonOperator(
        task_id='extract',
        python_callable=extract_data,
    )

    transform = PythonOperator(
        task_id='transform',
        python_callable=lambda: transform_data(extract.output),
    )

    load = PythonOperator(
        task_id='load',
        python_callable=load_data,
        op_kwargs={'df': transform.output},
    )

    extract >> transform >> load
