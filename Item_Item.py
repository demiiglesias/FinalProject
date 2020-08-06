import pandas as pd
# Algorithim for nearest neighbors
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix

# convert to matrix for computation of nearest neighbors

#Creates a data frame that reads in movies.csv file
movies_df = pd.read_csv('movies.csv', usecols=['movieId', 'title'])
#Creates a data frame that reads in ratings.csv file
rating_df = pd.read_csv('ratings.csv', usecols=['userId', 'movieId', 'rating'])
#merges dataframes
df = pd.merge(rating_df, movies_df, on='movieId')

# To remove date from "title" column
title_col = []

for x in df['title']:
    substring = x[:x.rfind("(") - 1]
    try:
        title_col.append(str(substring))
    except:
        title_col.append(x)

df['title'] = title_col

# drops NAN from dataframe
combine_movie_rating = df.dropna(axis=0, subset=['title'])

##splitting the combined movie rating dataframe by title and rating
temp_df = (combine_movie_rating.groupby(by=['title'])['rating'].count().reset_index())

# rename dataframe
movie_ratingCount = temp_df.rename(columns={'rating': 'totalRatingCount'})[['title', 'totalRatingCount']]

# merge combined movie ratings and count of total ratings
user_rating_with_count_ratings = combine_movie_rating.merge(movie_ratingCount, left_on='title', right_on='title',
                                                            how='left')

# Computes based off 3 significant figures
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# Checks whether total rating is greater than or equal to 50
popularity_threshold = 50
rate_popular_movie = user_rating_with_count_ratings.query('totalRatingCount >= @popularity_threshold')

movies = rate_popular_movie.pivot_table(index='title', columns='userId', values='rating').fillna(0)
# looks through all movies in title column and fills sparse graph values of 'NAN' with '0'

# creates dense matrix of movie titles
movies_df_matrix = csr_matrix(movies.values)

# use sklearn algorithim of nearest neighbors with cosine similarity metric
knn = NearestNeighbors(metric='cosine', algorithm='brute')
knn.fit(movies_df_matrix)


def rec(movie):
    additional_movies = []
    movie_index = 0

    # df.shape[0] gives number of rows in data frame
    for ind in range(movies.shape[0]):
        movie_name = movies.index.values[ind]
        if movie == movie_name:
            movie_index = ind

    # gets 10 closest neighbors to movie selected
    distances, indices = knn.kneighbors(movies.iloc[movie_index, :].values.reshape(1, -1), n_neighbors=10)

    for i in range(0, len(distances.flatten())):
        if i == 0:
            format(movies.index[movie_index])
        else:
            title = str('{1}'.format(i, movies.index[indices.flatten()[i]], distances.flatten()[i]))
            ########################################Uncomment below to see accuracy of similar movies to selected movie####################
            # distances closer to 0 represent a more similar movie
            #print('{0}: {1}, with distance of {2}:'.format(i, movies.index[indices.flatten()[i]], distances.flatten()[i]))

            # writes recommended movies to list to get retreived by GUI
            additional_movies.append(title)

    df_final = pd.DataFrame(additional_movies)
    return df_final[0].to_string(index=False)
