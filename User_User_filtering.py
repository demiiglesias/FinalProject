import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# from scipy import spatial
# result = 1 - spatial.distance.cosine(dataSetI, dataSetII)
# from numpy import dot
# from numpy.linalg import norm

# cos_sim = dot(a, b)/(norm(a)*norm(b))

# read files and create dataframes
movies = pd.read_csv("movies2.csv")
ratings = pd.read_csv("ratings.csv")


def find_movie_Id(movie):
    ID = -1
    # looks through all movies in title column
    for row in movies.itertuples():
        if movie == row.title:
            # ID is assigned to movie selected
            ID = row.movieId
    return ID


# Remove date from title
title_col = []

for x in movies['title']:
    substring = x[:x.rfind("(") - 1]
    try:
        title_col.append(str(substring))
    except:
        title_col.append(x)

movies['title'] = title_col


def write_to_file(convert):
    keys = []
    values = []
    # list of keys from dictionary convert of movie IDs
    keys_list = convert.keys()
    # list of values from dictionary convert from movie IDs
    values_list = convert.values()

    for key in keys_list:
        keys.append(key)

    for value in values_list:
        values.append(value)

    key1 = keys[0]
    value1 = values[0]
    float_value1 = float(value1)

    line1 = "611," + str(key1) + "," + str(float_value1) + ",1"

    # add user information to csv file, USER INFO IS REGISTERED AS USER 611
    with open("ratings.csv", 'a', newline='') as file:
        file.write("\n")
        file.write(line1)
    file.close()


# group userID and rating
mean = ratings.groupby(by="userId", as_index=False)['rating'].mean()
rating_avg = pd.merge(ratings, mean, on='userId')

# create an adjusted rating between the difference of compared users
rating_avg['adg_rating'] = rating_avg['rating_x'] - rating_avg['rating_y']

check = pd.pivot_table(rating_avg, values='rating_x', index='userId', columns='movieId')

final = pd.pivot_table(rating_avg, values='adg_rating', index='userId', columns='movieId')

# Fixes sparse graph issue by inserting NAN values with a integer
final_movie = final.fillna(final.mean(axis=0))
final_user = final.apply(lambda row: row.fillna(row.mean()), axis=1)


def create_cosine_similarity(final):
    # Creates cosine similarity values
    user_cosine = cosine_similarity(final)
    np.fill_diagonal(user_cosine, 0)
    similarity_with_user = pd.DataFrame(user_cosine, index=final.index)
    similarity_with_user.columns = final.index

    return similarity_with_user


# KNN Nearest neighbors algorithim
def find_n_neighbors(df, n):
    sort = np.argsort(df.values, axis=1)[:, :n]
    # updated dataframe with sorted values
    df = df.apply(lambda x: pd.Series(x.sort_values(ascending=False).iloc[:n].index,
                                      index=['Closest{}'.format(i) for i in range(1, n + 1)]), axis=1)
    return df


# top 30 neighbors for each user
users_in_neighborhood = find_n_neighbors(create_cosine_similarity(final_user), 30)
# top 30 neighbors for each user based off movie
movies_in_neighborhood = find_n_neighbors(create_cosine_similarity(final_movie), 30)

rating_avg = rating_avg.astype({"movieId": str})
Movie_user = rating_avg.groupby(by='userId')['movieId'].apply(lambda x: ','.join(x))


def User_item_score1(user):
    Movie_seen_by_user = check.columns[check[check.index == user].notna().any()].tolist()
    semi_list_container = movies_in_neighborhood[movies_in_neighborhood.index == user].values.squeeze().tolist()

    # put in list container
    # list_of_movies_used = movies_in_neighborhood.squeeze().tolist()

    d = Movie_user[Movie_user.index.isin(semi_list_container)]
    l = ','.join(d.values)

    Movie_seen_by_similar_users = l.split(',')
    # seperates movie titles in list

    Movies_under_consideration = list(set(Movie_seen_by_similar_users) - set(list(map(str, Movie_seen_by_user))))
    Movies_under_consideration = list(map(int, Movies_under_consideration))

    score = []
    for item in Movies_under_consideration:
        c = final_movie.loc[:, item]

        d = c[c.index.isin(semi_list_container)]

        f = d[d.notnull()]

        avg_user = mean.loc[mean['userId'] == user, 'rating'].values[0]
        index = f.index.values.squeeze().tolist()
        corr = create_cosine_similarity(final_user).loc[user, index]
        fin = pd.concat([f, corr], axis=1)
        fin.columns = ['adg_score', 'correlation']
        fin['score'] = fin.apply(lambda x: x['adg_score'] * x['correlation'], axis=1)

        top = fin['score'].sum()
        bottom = fin['correlation'].sum()
        final_score = avg_user + (top / bottom)
        score.append(final_score)

    data = pd.DataFrame({'movieId': Movies_under_consideration, 'score': score})
    top_5_recommendations = data.sort_values(by='score', ascending=False).head(5).merge(movies, how='inner',
                                                                                        on='movieId').title.values.tolist()
    # list of top recpmmendations movies

    return top_5_recommendations


""" # list of movies in dataframe of 30
    semi_list_of_movies = movies_in_neighborhood[movies_in_neighborhood.index == user].values
    # create a list container
    adj_list_of_movies = semi_list_of_movies.squeeze().tolist()
    # list of movies to be used from pivot table of avg values
    located_movies = final_movie.loc[:, item]

    search = located_movies[located_movies.index.isin(adj_list_of_movies)]

    # checks to see item is not null
    checker = search[search.notnull()]

    # update avg user information with UserId and the rating of user
    avg_user = mean.loc[mean['userId'] == user, 'rating'].values[0]

    # put info in a list container
    index = checker.index.values.squeeze().tolist()

    # find correlation
    corr = similarity_with_movie.loc[user, index]

    # create new dataframe with updated avg infromation
    fin = pd.concat([checker, corr], axis=1)
    fin.columns = ['adjusted_score', 'correlation']
    fin['score'] = fin.apply(lambda x: x['adjusted_score'] * x['correlation'], axis=1)

    # final score = given by avg_user rating rating + sum(score/correlation)
    top = fin['score'].sum()
    bottom = fin['correlation'].sum()
    final_score = avg_user + (top / bottom)
    return final_score"""

# last row of dataframe = active user
user = ratings.iloc[-1]['userId']


def GUI_Output():
    list_ = []
    # predicts movies based off user-user score and returns list of movies recommended to user that user would like
    recommended_movies = User_item_score1(user)

    for i in recommended_movies:
        list_.append(i)

    return list_
