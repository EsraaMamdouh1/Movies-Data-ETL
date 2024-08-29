import pandas as pd
import numpy as np

print("Reading ratings data...")
# Create a DataFrame for Movie Ratings
ratings = pd.read_csv('/data/ml-100k/u.data', delimiter='\t', header=None, names=['user_id', 'item_id', 'rating', 'timestamp'])
print("Ratings data read successfully.")

print("Processing movie names...")
# Create a DataFrame for Movie Names
with open('/data/ml-100k/u.item', 'r', encoding="ISO-8859-1") as read_file:
    movies_df = pd.DataFrame(columns=['item_id', 'movie_name', 'release_timestamp'])

    for line in read_file:
        fields = line.split('|')
        item_id, movie_name, release_timestamp = fields[0], fields[1], fields[2]
        movie_name = movie_name[0:len(movie_name) - len(' (1234)')]
        line_data = [int(item_id), str(movie_name), release_timestamp]
        temp_df = pd.DataFrame(data=[line_data], columns=['item_id', 'movie_name', 'release_timestamp'])
        movies_df = pd.concat([temp_df, movies_df], ignore_index=True)

    movies_df.sort_values(by='item_id', ascending=True, inplace=True)

print("Movies data processed successfully.")

# Export to CSV
print("Exporting ratings to CSV...")
ratings.to_csv('/data/ratings.csv', index=False)
print("Ratings data exported successfully.")

print("Exporting movies to CSV...")
movies_df.to_csv('/data/movies.csv', index=False)
print("Movies data exported successfully.")

