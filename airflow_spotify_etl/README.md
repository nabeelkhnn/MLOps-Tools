# Airflow Spotify ETL

## Project Overview
This project is an educational exploration into Apache Airflow, focusing on its use in orchestrating an ETL pipeline. The ETL process extracts data from Spotify's API, transforms it, and loads it into a CSV file for analysis. Through this project, users can gain practical experience with Airflow's operational aspects, such as DAG configuration, task scheduling, and automation.

## Files Description
- `spotify_etl.py`: The core ETL script that interfaces with Spotify's API to extract track data, transforms it into a structured format, and loads the data into `spotify_tracks_data.csv`.
- `spotify_tracks_data.csv`: The output CSV file containing structured Spotify track data ready for analysis.
- `spotify_tracks_eda.ipynb`: A Jupyter notebook for exploratory data analysis on the Spotify track data, including visualizations and insights.
- `DAG file`: An Airflow script that defines the Directed Acyclic Graph for the ETL workflow, including task scheduling and dependencies.

## DAG File Explained
The provided DAG file sets up the Airflow workflow for our ETL process. The configuration includes defining the start date and managing the task to execute the ETL script. The `PythonOperator` is used to invoke the `run_spotify_etl` function, seamlessly integrating our ETL script within Airflow's managed environment.

## ETL File Explained
The `spotify_etl.py` script is a representation of the ETL process in action. Utilizing the `spotipy` library, the script authenticates with Spotify's API, fetches track data, and processes it into a pandas DataFrame. This DataFrame is then cleaned, processed, and saved to a CSV file, showcasing typical ETL steps such as data cleaning and feature extraction.

## Educational Purpose
The creation of this project is meant for educational purposes, demonstrating how Airflow can be employed to schedule, execute, and manage data workflows. The DAG file and ETL script provide concrete examples of Airflow's functionalities in a real-world ETL scenario.

## Running the ETL Pipeline
To run the ETL pipeline:
1. Start the Airflow web server with `airflow webserver -p 8080`.
2. Initiate the Airflow scheduler with `airflow scheduler`.
3. Access the Airflow UI through your web browser at `http://localhost:8080`.
4. Enable and trigger the `spotify_etl_dag` to begin the ETL process.

## Exploratory Data Analysis (EDA) Notebook
The EDA notebook conducts a thorough analysis of the Spotify track data. It includes data cleaning (e.g., removing duplicates, filling missing values), feature engineering (e.g., extracting year and month from release dates), and various exploratory analyses (e.g., calculating mean popularity by artist and release year).

## Contributions
Contributions are welcome. Please fork this repository, make your changes, and submit a pull request for review.

## License
This project is open-sourced under the MIT License. See the LICENSE file for full details.

## Contact
If you have any questions or need further assistance with this project, feel free to open an issue in the repository.


