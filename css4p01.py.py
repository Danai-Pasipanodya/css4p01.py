# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:00:51 2024

@author: danai
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('movie_dataset.csv')
df.columns = df.columns.str.replace(' ', '_')


movie_column = 'Title'
rating_column = 'Rating'

# Find the row with the highest rating
highest_rated_movie = df.loc[df[rating_column].idxmax()]

# Print the result
print(f"The highest-rated movie is '{highest_rated_movie[movie_column]}' with a rating of {highest_rated_movie[rating_column]}")

revenue_column = 'Revenue_(Millions)'

# Calculate the average revenue
average_revenue = df[revenue_column].mean()

# Print the result
print(f"The average revenue of all movies is: {average_revenue}")

# Assuming the dataset has columns 'Release_Year' and 'Revenue', replace them with your actual column names
release_year_column = 'Year'
revenue_column = 'Revenue_(Millions)'

# Filter movies released from 2015 to 2017
filtered_df = df[(df[release_year_column] >= 2015) & (df[release_year_column] <= 2017)]

# Calculate the average revenue for the filtered dataset
average_revenue_2015_to_2017 = filtered_df[revenue_column].mean()

# Print the result
print(f"The average revenue of movies from 2015 to 2017 is: {average_revenue_2015_to_2017}")

# Assuming the dataset has a 'Release_Year' column, replace it with your actual column name
release_year_column = 'Year'

# Count the number of movies released in the year 2016
movies_2016_count = len(df[df[release_year_column] == 2016])

# Print the result
print(f"The number of movies released in the year 2016 is: {movies_2016_count}")

# Assuming the dataset has a 'Director' column, replace it with your actual column name
director_column = 'Director'

# Count the number of movies directed by Christopher Nolan
nolan_movies_count = len(df[df[director_column] == 'Christopher Nolan'])

# Print the result
print(f"The number of movies directed by Christopher Nolan is: {nolan_movies_count}")

# Assuming the dataset has a 'Rating' column, replace it with your actual column name
rating_column = 'Rating'

# Count the number of movies with a rating of at least 8.0
highly_rated_movies_count = len(df[df[rating_column] >= 8.0])

# Print the result
print(f"The number of movies with a rating of at least 8.0 is: {highly_rated_movies_count}")

# Assuming the dataset has 'Director' and 'Rating' columns, replace them with your actual column names
director_column = 'Director'
rating_column = 'Rating'

# Filter movies directed by Christopher Nolan
nolan_movies = df[df[director_column] == 'Christopher Nolan']

# Calculate the median rating for Christopher Nolan's movies
median_rating_nolan = nolan_movies[rating_column].median()

# Print the result
print(f"The median rating of movies directed by Christopher Nolan is: {median_rating_nolan}")

# Assuming the dataset has 'Year' and 'Rating' columns, replace them with your actual column names
release_year_column = 'Year'
rating_column = 'Rating'

# Calculate the average rating for each year
average_ratings_by_year = df.groupby(release_year_column)[rating_column].mean()

# Find the year with the highest average rating
year_highest_avg_rating = average_ratings_by_year.idxmax()
highest_avg_rating = average_ratings_by_year.max()

# Print the result
print(f"The year with the highest average rating is {year_highest_avg_rating} with an average rating of {highest_avg_rating}")

# Assuming the dataset has a 'Year' column, replace it with your actual column name
release_year_column = 'Year'

# Filter movies released between 2006 and 2016 (inclusive)
movies_2006_to_2016 = df[(df[release_year_column] >= 2006) & (df[release_year_column] <= 2016)]

# Calculate the number of movies in each year
movies_count_2006 = len(df[df[release_year_column] == 2006])
movies_count_2016 = len(df[df[release_year_column] == 2016])

# Calculate the percentage increase
percentage_increase = ((movies_count_2016 - movies_count_2006) / movies_count_2006) * 100

# Print the result
print(f"The percentage increase in the number of movies between 2006 and 2016 is: {percentage_increase:.2f}%")

# Assuming the dataset has an 'Actors' column, replace it with your actual column name
actors_column = 'Actors'

# Concatenate all actor names into a single string
all_actors_str = ', '.join(df[actors_column].dropna())

# Split the concatenated string into a list of actors
all_actors_list = [actor.strip() for actor in all_actors_str.split(',')]

# Find the most common actor
most_common_actor = max(set(all_actors_list), key=all_actors_list.count)

# Print the result
print(f"The most common actor in all movies is: {most_common_actor}")

# Assuming the dataset has a 'Genres' column, replace it with your actual column name
genres_column = 'Genre'

# Extract unique genres from the dataset
unique_genres = df[genres_column].str.split(',').explode().str.strip().unique()

# Count the number of unique genres
num_unique_genres = len(unique_genres)

# Print the result
print(f"The number of unique genres in the dataset is: {num_unique_genres}")

# Assuming the dataset has 'Runtime' and 'Revenue' columns, replace them with your actual column names
runtime_column = 'Runtime_(Minutes)'
revenue_column = 'Revenue_(Millions)'

# Extract relevant columns for correlation analysis
selected_columns = [runtime_column, revenue_column]
selected_data = df[selected_columns]

# Calculate the correlation coefficient between 'Runtime' and 'Revenue'
correlation_coefficient = selected_data.corr().iloc[0, 1]

# Print the correlation coefficient
print(f"The correlation coefficient between 'Runtime' and 'Revenue' is: {correlation_coefficient:.2f}")