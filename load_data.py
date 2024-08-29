import shutil
import os

# Define the destination directory (simulating a bucket)
destination_dir = '/data/uploaded'

# Ensure the directory exists
os.makedirs(destination_dir, exist_ok=True)

def upload_to_local(blob_name, file_path):
    try:
        # Define the destination path
        destination_path = os.path.join(destination_dir, blob_name)

        # Copy the file to the local directory
        shutil.copy(file_path, destination_path)
        print(f'File {blob_name} uploaded successfully to {destination_path}.')
        return True
    except Exception as e:
        print(e)
        return False

# Specify the path to the CSV files
movies_path = '/data/movies.csv'
ratings_path = '/data/ratings.csv'

# Upload CSV files to the local directory
upload_to_local(blob_name='movies.csv', file_path=movies_path)
upload_to_local(blob_name='ratings.csv', file_path=ratings_path)
