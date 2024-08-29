# Movies Data ETL using Docker

The goal of this ETL process is to extract movie ratings data, process it, and store it in a local storage setup using Docker. This project simulates the ETL process without relying on cloud services, making it suitable for local or on-premise environments.

## Project Architecture

![Project Architecture](data/Movies_Data_Pipeline2.png)

## Steps

1. **Download ratings and movies data**: Use the provided bash script to download the dataset from [MovieLens](https://files.grouplens.org/datasets/movielens).

2. **Process the Data and Export to CSV**:
    - The Python scripts process the raw data, transform it into the desired format, and save it locally.

3. **Run the Docker Container**:
    - The entire ETL process is encapsulated within a Docker container for easy setup and portability.
    - Build the Docker image:
      ```bash
      docker build -t movies_data_etl .
      ```
    - Run the ETL process inside the Docker container:
      ```bash
      docker run --rm movies_data_etl
      ```

## Pre-requisites

- **Docker**: Ensure Docker is installed and running on your machine.
- **Python 3.x**: Required to run the Python scripts if not using Docker.

## Applying The ETL Process

### 1. Download Data:
```bash
bash download_data.sh

### 2. Run the ETL process:
```bash
bash python movies_etl.py

## End Result:

![Uploaded Files in Docker Container](data\uploaded_files.png)
