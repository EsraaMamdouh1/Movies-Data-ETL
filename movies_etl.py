from Helper import LocalStorageHelper

# Create an instance of class: LocalStorageHelper
helper = LocalStorageHelper()

# Create directories for CSV files
helper.create_directory('/data/uploaded')

# Process the ratings and movies files into DataFrames
ratings = helper.process_ratings(file_path='/data/ml-100k/u.data')
movies = helper.process_movies(file_path='/data/ml-100k/u.item')

# Export DataFrames to CSV
helper.export_dataframe_to_csv(dataframe=ratings, csv_name='/data/ratings')
helper.export_dataframe_to_csv(dataframe=movies, csv_name='/data/movies')

# Copy CSV files to the upload directory (simulating upload to local storage)
helper.copy_file(source_path='/data/ratings.csv', dest_path='/data/uploaded/ratings.csv')
helper.copy_file(source_path='/data/movies.csv', dest_path='/data/uploaded/movies.csv')
