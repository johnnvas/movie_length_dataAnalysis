# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
netflix_df = pd.read_csv('netflix_data.csv')
netflix_subset = netflix_df[netflix_df['type'] == "Movie"]

print(netflix_subset.head(50))
