import pandas as pd
import warnings
# import time
from ast import literal_eval

warnings.simplefilter('ignore')
# start_time = time.time()
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

df = pd.read_csv('movies_metadata.csv',
                 usecols=['genres', 'popularity', 'poster_path', 'runtime', 'title', 'vote_average', 'vote_count'])
df = df.drop([19730, 29503, 35587])

df['genres'] = df['genres'].fillna('[]').apply(literal_eval).apply(
    lambda x: [i['name'] for i in x] if isinstance(x, list) else [])


def get_movies_from_genre(genre_str):
    genre_df = df
    genre_df['popularity'] = genre_df['popularity'].astype('float')
    filt = genre_df['genres'].apply(lambda y: genre_str in y)
    genre_df = genre_df[filt].sort_values('popularity', ascending=False)
    genre_df = genre_df[0:2]['title']
    return genre_df.to_string(index=False)


# print(get_movies_from_genre('Comedy'))
# print("(*Last) Time elapsed: {:.2f}s".format(time.time() - start_time))

