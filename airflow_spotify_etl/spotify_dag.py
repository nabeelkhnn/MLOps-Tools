import sys
import os

# Path to the directory containing your ETL script (spotify_etl.py)
etl_script_directory = '/Users/nabeel/Desktop/Projects/'

# Ensure the directory path is in the absolute format
etl_script_directory = os.path.abspath(etl_script_directory)

# Insert the directory path to sys.path
if etl_script_directory not in sys.path:
    sys.path.insert(0, etl_script_directory)

# Now you can import functions from your ETL script (spotify_etl.py)
from spotify_etl import run_spotify_etl



from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Import the function from your ETL script
from spotify_etl import run_spotify_etl

# Define default arguments for the DAG
default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 8),  # Set the start date
    'retries': 1,
}

# Create a DAG instance
dag = DAG(
    'spotify_etl_dag',
    default_args=default_args,
    description='ETL process for Spotify data',
    schedule_interval=None,  # Set the schedule interval as needed
)

# Define a PythonOperator to run your ETL function
run_etl_task = PythonOperator(
    task_id='run_spotify_etl_task',
    python_callable=run_spotify_etl,
    dag=dag,
)

# Define the task dependencies
run_etl_task

if __name__ == "__main__":
    dag.cli()