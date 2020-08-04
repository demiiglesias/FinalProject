import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def find_movie_Id(movie):
    ID = -1
    # looks through all movies in title column
    for row in movies.itertuples():
        if movie == row.title:
            # ID is assigned to movie selected
            ID = row.movieId
    return ID

# creates movie dataframe
movies = pd.read_csv("movies.csv")

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
    #list of keys
    keys_list = convert.keys()
    #list of values
    values_list = convert.values()

    for key in keys_list:
        keys.append(key)

    for value in values_list:
        values.append(value)

    key1 = keys[0]
    value1 = values[0]
    float_value1 = float(value1)

    line1 = "611," + str(key1) +"," + str(float_value1) + ",1"

    key2 = keys[1]
    value2 = values[1]
    float_value2 = float(value2)

    line2 = "611," + str(key2) +"," + str(float_value2) + ",1"

    key3 = keys[2]
    value3 = values[2]
    float_value3 = float(value3)

    line3 = "611," + str(key3) + "," + str(float_value3) + ",1"

    key4 = keys[3]
    value4 = values[3]
    float_value4 = float(value4)

    line4 = "611," + str(key4) + "," + str(float_value4) + ",1"

    key5 = keys[4]
    value5 = values[4]
    float_value5 = float(value5)

    line5 = "611," + str(key5) +"," + str(float_value5) + ",1"

    # add user information to csv file, USER INFO IS REGISTERED AS USER 611
    with open("ratings.csv",'a', newline='') as file:
        file.write("\n")
        file.write(line1)
        file.write("\n")
        file.write(line2)
        file.write("\n")
        file.write(line3)
        file.write("\n")
        file.write(line4)
        file.write("\n")
        file.write(line5)
        file.close()


ratings = pd.read_csv("ratings.csv")
tags = pd.read_csv("tags.csv")
# group userID and rating
mean = ratings.groupby(by="userId", as_index=False)['rating'].mean()
rating_avg = pd.merge(ratings, mean, on='userId')
rating_avg['adg_rating'] = rating_avg['rating_x']
rating_avg['rating_y']
rating_avg.head()

movies.head()
ratings.head()
tags.head()

check = pd.pivot_table(rating_avg, values='rating_x', index='userId', columns='movieId')
check.head()

final = pd.pivot_table(rating_avg, values='adg_rating', index='userId', columns='movieId')

final_movie = final.fillna(final.mean(axis=0))
final_movie.head()

final_user = final.apply(lambda row: row.fillna(row.mean()), axis=1)
final_user.head()

# user similarity on replacing NAN by user  avg
cosine = cosine_similarity(final_user)
np.fill_diagonal(cosine, 0)
similarity_with_user = pd.DataFrame(cosine, index=final_user.index)
similarity_with_user.columns = final_user.index
similarity_with_user.head()

# user similarity on replacing NAN by movie avg
cosine_B = cosine_similarity(final_movie)
np.fill_diagonal(cosine_B, 0)
similarity_with_movie = pd.DataFrame(cosine_B, index=final_movie.index)
similarity_with_movie.columns = final_user.index
similarity_with_movie.head()


# KNN Nearest neighbors
def find_n_neighbors(df, n):
    order = np.argsort(df.values, axis=1)[:, :n]
    df = df.apply(lambda x: pd.Series(x.sort_values(ascending=False).iloc[:n].index,
                                      index=['top{}'.format(i) for i in range(1, n + 1)]), axis=1)
    return df


# top 30 neighbors for each user
sim_user_30 = find_n_neighbors(similarity_with_user, 10)
sim_user_30.head()

# top 30 neighbors for each user
sim_user_30_b = find_n_neighbors(similarity_with_movie, 10)
sim_user_30_b.head()


def get_user_similar_movies(user1, user2):
    common_movies = rating_avg[rating_avg.userId == user1].merge(rating_avg[rating_avg.userId == user2], on='movieId',
                                                                 how='inner')
    return common_movies.merge(movies, on='movieId')


a = get_user_similar_movies(370, 86309)
a = a.loc[:, ['rating_x_x', 'rating_x_y', 'title']]
a.head()

# def User_item_score(user,item):
#   a = sim_user_30_b[sim_user_30_b.index == user].values
#  b = a.squeeze().tolist()
#   c = final_movie.loc[:, item]
#  d = c[c.index.isin(b)]
#  f = d[d.notnull()]
#  avg_user = mean.loc[mean['userId'] == user, 'rating'].values[0]
# index = f.index.values.squeeze().tolist()
# corr = similarity_with_movie.loc[user, index]
# fin = pd.concat([f, corr], axis=1)
# fin.columns = ['adg_score', 'correlation']
# fin['score'] = fin.apply(lambda x: x['adg_score'] * x['correlation'], axis=1)
# nume = fin['score'].sum()
# deno = fin['correlation'].sum()
# final_score = avg_user + (nume / deno)
# return final_score

# score = User_item_score(320,7371)
# print("score(u,i) is", score)

rating_avg = rating_avg.astype({"movieId": str})
Movie_user = rating_avg.groupby(by='userId')['movieId'].apply(lambda x: ','.join(x))


def User_item_score1(user):
    Movie_seen_by_user = check.columns[check[check.index == user].notna().any()].tolist()
    a = sim_user_30_b[sim_user_30_b.index == user].values
    b = a.squeeze().tolist()
    d = Movie_user[Movie_user.index.isin(b)]
    l = ','.join(d.values)
    Movie_seen_by_similar_users = l.split(',')
    Movies_under_consideration = list(set(Movie_seen_by_similar_users) - set(list(map(str, Movie_seen_by_user))))
    Movies_under_consideration = list(map(int, Movies_under_consideration))
    score = []
    for item in Movies_under_consideration:
        c = final_movie.loc[:, item]
        d = c[c.index.isin(b)]
        f = d[d.notnull()]
        avg_user = mean.loc[mean['userId'] == user, 'rating'].values[0]
        index = f.index.values.squeeze().tolist()
        corr = similarity_with_movie.loc[user, index]
        fin = pd.concat([f, corr], axis=1)
        fin.columns = ['adg_score', 'correlation']
        fin['score'] = fin.apply(lambda x: x['adg_score'] * x['correlation'], axis=1)
        nume = fin['score'].sum()
        deno = fin['correlation'].sum()
        final_score = avg_user + (nume / deno)
        score.append(final_score)
    data = pd.DataFrame({'movieId': Movies_under_consideration, 'score': score})
    top_5_recommendation = data.sort_values(by='score', ascending=False).head(5)
    Movie_Name = top_5_recommendation.merge(movies, how='inner', on='movieId')
    Movie_Names = Movie_Name.title.values.tolist()
    return Movie_Names


# last row of dataframe = active user
user = ratings.iloc[-1]['userId']


def GUI_Output():
    list = []
    predicted_movies = User_item_score1(user)

    for i in predicted_movies:
        list.append(i)

    return list

