# Use the official Python image from the Docker Hub
FROM python:3.11

# Set the working directory in the container
WORKDIR /data

# Copy the Python scripts into the container
COPY movies_etl.py ./
COPY Helper.py ./

# Run the ETL script
CMD ["python", "movies_etl.py"]
