import collections
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Organizing Data into maps
# Import Movie Data from CSV file
df = pd.read_csv('p3_scrape.csv')

# converting it to a data frame
df = df[['Title', 'Genre', 'Director']]
df.head()
print(df)
# Keeps track of movie titles only
genre = 'Drama'
count = CountVectorizer()
count_matrix = count.fit_transform(df['Genre'])

# Cosine sim Matrix
similarity = cosine_similarity(count_matrix, count_matrix)

indices = pd.Series(df.index)


def recommendations(genre, similarity=similarity):
    movie_recommendations = []

    # index of movie matching title
    indx = indices[indices == genre].index[0]

    # Series has cosine scores descending order
    score = pd.Series(similarity[indx]).sort_values(ascending=False)
    top_5 = list(score.iloc[1:6].index)

    # Adding top 5 titles to movie_recommendations
    for i in top_5:
        movie_recommendations.append(list(df.index)[i])

    return print(movie_recommendations)
