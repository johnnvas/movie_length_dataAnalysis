# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
netflix_df = pd.read_csv('netflix_data.csv')
netflix_subset = netflix_df[netflix_df['type'] == "Movie"]

netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]
short_movies = netflix_movies[netflix_movies['duration'] < 60]

print(short_movies.head(50))
