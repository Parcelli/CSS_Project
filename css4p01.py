#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:26:18 2024

@author: parcelli
"""

#Extract,transform and load movie dataset in python using pandas library
import pandas as pd
#Loading data either from local files
df= pd.read_csv("/home/parcelli/css2024_day1/movie_dataset.csv",index_col=0)
print(df)

#Cleaning data
#Removing spaces on the column headers and replacing with nothing
print(df.columns)
df.columns = df.columns.str.replace(' ', '') 
print(df.columns)

#Removing rows with missing values
#Removing rows with missing values
df.dropna(inplace = True)
df = df.reset_index(drop=True)

#Checking for duplicates
sum(df.duplicated())

#Finding highest rated movie

highest_rated_movie = df.sort_values(by='Rating', ascending=False).head(1)
print(highest_rated_movie)

#Finding average revenue
average_revenue=df["Revenue(Millions)"].mean()
print(average_revenue)

#Movies released in 2016
#Filter movies released in 2016
movies_2016= df[df['Year'] == 2016]
#Count movies in the filtered data
movies_2016.count()

#Movies directed by Christopher Nolan
#Filter movies
movies_ChrisNolan= df[df['Director'] == 'Christopher Nolan']
#Count movies in the filtered data
movies_ChrisNolan.count()

#Movies with ratings of atleast 8.0
#Filter movies
movies_8_rating= df[df['Rating'] >= 8.0]
#Count movies in the filtered data
movies_8_rating.count()

#The year with the highest average rating
#Group data per year and find mean rating for each year
average_rating=df.groupby('Year')['Rating'].mean()
print(average_rating)
average_rating.max()

#median rating of movies directed by Christopher Nolan
#Using earlier filtered data of movies directed by Christopher Nolan
movies_ChrisNolan['Rating'].median()

# Find the most common actor
all_actors = df['Actors'].str.split(', ').explode()
most_common_actor = all_actors.mode().iloc[0]

# Combine all genre strings into a single list and split by ', '
all_genres = df['Genre'].str.split(', ').explode()

# Count the unique genres
unique_genres = all_genres.nunique()



