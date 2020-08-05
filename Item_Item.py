import pandas as pd
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors


def rec(movie):
    additional_movies = []
    movies_df = pd.read_csv('movies.csv', usecols=['movieId', 'title'])
    rating_df = pd.read_csv('ratings.csv', usecols=['userId', 'movieId', 'rating'])
    # movies_df = pd.read_csv('movies.csv', usecols=['movieId', 'title'], dtype={'movieId': 'int32', 'title': 'str'})
    # rating_df = pd.read_csv('ratings.csv', usecols=['userId', 'movieId', 'rating'],
    # dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})

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

    # drops title from dataframe

    combine_movie_rating = df.dropna(axis=0, subset=['title'])
    movie_ratingCount = (combine_movie_rating.
        groupby(by=['title'])['rating'].
        count().
        reset_index().
        rename(columns={'rating': 'totalRatingCount'})
    [['title', 'totalRatingCount']])

    rating_with_totalRatingCount = combine_movie_rating.merge(movie_ratingCount, left_on='title', right_on='title',
                                                              how='left')
    rating_with_totalRatingCount.head()

    # Computes based off 3 signficant figures
    pd.set_option('display.float_format', lambda x: '%.3f' % x)

    # Threshold represents
    popularity_threshold = 50
    rating_popular_movie = rating_with_totalRatingCount.query('totalRatingCount >= @popularity_threshold')

    movie_features_df = rating_popular_movie.pivot_table(index='title', columns='userId', values='rating').fillna(0)
    # looks through all movies in title column and fills sparse graph values of 'NAN' with '0'

    # Place holder for query index, begins at "10 Things I Hate About You (1999)
    query_index = 0

    # df.shape[0] gives number of rows in data frame
    for ind in range(movie_features_df.shape[0]):
        movie_name = movie_features_df.index.values[ind]
        if movie == movie_name:
            query_index = ind

    # convert to matrix for computation of nearest neighbors
    movie_features_df_matrix = csr_matrix(movie_features_df.values)

    model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
    model_knn.fit(movie_features_df_matrix)

    # gets 15 closest neighbors to movie selected
    distances, indices = model_knn.kneighbors(movie_features_df.iloc[query_index, :].values.reshape(1, -1),
                                              n_neighbors=10)

    for i in range(0, len(distances.flatten())):
        if i == 0:
            format(movie_features_df.index[query_index])
        else:
            title = str('{1}'.format(i, movie_features_df.index[indices.flatten()[i]], distances.flatten()[i]))
            # writes recommended movies to list
            additional_movies.append(title)

    # print("movie_features_df: ")
    # print(movie_features_df)
    # print()
    #
    # letters = {'A', 'B', 'C'}
    # for i in letters:
    #     print("Letters List: ")
    #     print(i)

    # additional_movies = movie_features_df['title']
    # additional_movies = additional_movies
    # print("Type of additional_movies")
    # print(type(additional_movies))

    return additional_movies


# def fix_me(movies):
#
#
#     return movies


