import os
import shutil
import pandas as pd

class LocalStorageHelper:

    def __init__(self):
        pass

    def create_directory(self, dir_path):
        """
        Create a directory if it does not exist.

        Args:
            dir_path (str): Path to the directory.

        Returns:
            bool: True if directory creation was successful, False otherwise.
        """
        try:
            os.makedirs(dir_path, exist_ok=True)
            print(f'Directory {dir_path} created successfully.')
            return True
        except Exception as e:
            print(f"Error creating directory: {e}")
            return False

    def process_ratings(self, file_path='ml-100k/u.data'):
        """
        Create a DataFrame of movie ratings from the file.

        Args:
            file_path (str): Path to the 'u.data' file.

        Returns:
            pd.DataFrame: DataFrame containing movie ratings.
        """
        try:
            ratings = pd.read_csv(file_path, delimiter='\t', header=None, names=['user_id', 'item_id', 'rating', 'timestamp'])
            return ratings
        except Exception as e:
            print(f"Error processing ratings: {e}")
            return None

    def process_movies(self, file_path='ml-100k/u.item'):
        """
        Create a DataFrame of movie names from the file.

        Args:
            file_path (str): Path to the 'u.item' file.

        Returns:
            pd.DataFrame: DataFrame containing movie names and details.
        """
        try:
            with open(file_path, 'r', encoding="ISO-8859-1") as read_file:
                movies_df = pd.DataFrame(columns=['item_id', 'movie_name', 'release_timestamp'])
                for line in read_file:
                    fields = line.split('|')
                    item_id, movie_name, release_timestamp = fields[0], fields[1], fields[2]
                    movie_name = movie_name.split(' (')[0]
                    line_data = [int(item_id), str(movie_name), release_timestamp]
                    temp_df = pd.DataFrame(data=[line_data], columns=['item_id', 'movie_name', 'release_timestamp'])
                    movies_df = pd.concat([temp_df, movies_df], ignore_index=True)
                movies_df.sort_values(by='item_id', ascending=True, inplace=True)
                return movies_df
        except Exception as e:
            print(f"Error processing movies: {e}")
            return None

    def export_dataframe_to_csv(self, dataframe, csv_name):
        """
        Export DataFrame to CSV.

        Args:
            dataframe (pd.DataFrame): DataFrame to export.
            csv_name (str): Name of the CSV file (without extension).

        Returns:
            bool: True if export was successful, False otherwise.
        """
        try:
            dataframe.to_csv(f'{csv_name}.csv', index=False)
            print(f'DataFrame exported to {csv_name}.csv successfully.')
            return True
        except Exception as e:
            print(f"Error exporting DataFrame to CSV: {e}")
            return False

    def copy_file(self, source_path, dest_path):
        """
        Copy a file from source to destination.

        Args:
            source_path (str): Path to the source file.
            dest_path (str): Path to the destination file.

        Returns:
            bool: True if file copy was successful, False otherwise.
        """
        try:
            shutil.copy(source_path, dest_path)
            print(f'File copied from {source_path} to {dest_path}.')
            return True
        except Exception as e:
            print(f"Error copying file: {e}")
            return False
