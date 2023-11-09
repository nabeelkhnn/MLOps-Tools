# Airflow Spotify ETL

## Project Overview
This project is a hands-on exploration of Apache Airflow, designed to orchestrate an ETL pipeline that interacts with Spotify's API. Specifically, it processes data from the "Billboard Top 100" playlist, focusing on the relationship between track popularity and the release date. This practical application allows users to gain insights into Airflow’s DAG configuration, task scheduling, and the automation of complex data workflows.

## Problem Statement
In the data-dense digital landscape of the music industry, there is a critical need to efficiently manage the workflow for extracting and analyzing data. **This project addresses the need to automate the data workflow for Spotify's "Billboard Top 100" playlist, aiming to examine how a track's popularity correlates with its release timing.** The challenge lies in the efficient and systematic extraction, transformation, and loading of track data for insightful analysis.

## Files Description
- `spotify_etl.py`: Executes the ETL process, interfacing with Spotify’s API to fetch "Billboard Top 100" track data, transforming and loading it into a CSV file.
- `spotify_tracks_data.csv`: Contains the processed data of Spotify tracks, ready for analytical interrogation.
- `spotify_tracks_eda.ipynb`: A Jupyter notebook for exploratory data analysis, focusing on the popularity and temporal trends within the "Billboard Top 100" playlist data.
- `DAG file`: Defines the Airflow DAG for the ETL workflow, scheduling and orchestrating the tasks.

## DAG File Explained
The DAG file is the backbone of the ETL process within Airflow, initiating the start date and task execution strategy. It utilizes the `PythonOperator` to call the `run_spotify_etl` function, integrating our specific ETL requirements into Airflow's ecosystem.

## ETL File Explained
`spotify_etl.py` is tailored for real-world application, leveraging the `spotipy` library to authenticate and retrieve data from Spotify's "Billboard Top 100" playlist. The script processes the data into a pandas DataFrame, illustrating key ETL operations such as data cleansing and attribute extraction.

## Educational Purpose
This project serves an educational role, demonstrating Airflow's capabilities in scheduling and managing data workflows. It provides tangible examples of constructing and deploying a data pipeline for an actual ETL task.

## Running the ETL Pipeline
Instructions are provided to initialize and navigate Airflow's UI to run the customized `spotify_etl_dag`.

## Exploratory Data Analysis (EDA) Notebook
The EDA notebook delves into the "Billboard Top 100" data, employing statistical methods to explore the dynamics between track popularity and release dates, among other attributes.

## Personal Touch
As the architect of this project, I, `Nabeel Khan`, have intertwined my expertise in data engineering with a deep interest in music analytics. Each code segment and analytical query is a testament to a diligent and meticulous approach, ensuring a project that is not only functional but also a reflection of a genuine passion for data and music.

## Contributions
For those interested in contributing, guidelines are provided to encourage community involvement and enhancement of the project.

## License
The project is shared openly under the MIT License.

## Contact
An invitation is extended for questions or further assistance, promoting an interactive community around this project.
