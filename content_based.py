import pandas as pd
import numpy as np
import warnings
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.snowball import SnowballStemmer
from ast import literal_eval

warnings.simplefilter('ignore')

# =================  Display Settings =================
desired_width = 640
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

# =================  Reading the CSV Files =================
df = pd.read_csv('movies_metadata.csv',
                 usecols=['genres', 'id', 'overview', 'popularity', 'poster_path', 'release_date', 'runtime',
                          'spoken_languages', 'tagline', 'title', 'vote_average', 'vote_count'])
keywords = pd.read_csv('keywords.csv')
credits = pd.read_csv('credits.csv')

# =================  Prep before Merge on 'id' =================
# converting the id column, of all the files, into integers
keywords['id'] = keywords['id'].astype('int')
credits['id'] = credits['id'].astype('int')

# fixing movies_metadata before converting
# These rows were in a different format (xxxx-xx-xx), and most of the df was bad (NaN) or out of place
df = df.drop([19730, 29503, 35587])
df['id'] = df['id'].astype('int')

# =================  Merge on the 'id' column =================
# merging movies_metadata with credits and keywords based on the 'id' column
df = df.merge(credits, on='id')
df = df.merge(keywords, on='id')

# =================  Prep before possibly using get_smaller_df =================
# Changing Genres
df['genres'] = df['genres'].fillna('[]').apply(literal_eval).apply(
    lambda x: [i['name'] for i in x] if isinstance(x, list) else [])

# Using 'release_date' (1995-12-15) to make and append a new column named 'year' (1995)
df['year'] = pd.to_datetime(df['release_date'], errors='coerce').apply(
    lambda x: str(x).split('-')[0] if x != np.nan else np.nan)


def get_smaller_df(x):
    links_small = pd.read_csv('links_small.csv', usecols=['tmdbId'])
    links_small = links_small[links_small['tmdbId'].notnull()]['tmdbId'].astype('int')
    # Only rows having links_small's number under 'id' can remain. Dataframe goes from 46628 to 9219 rows
    x = x[x['id'].isin(links_small)]
    x['popularity'] = x['popularity'].astype('float')
    x['runtime'] = x['runtime'].astype('float')
    # After the conditions below the dfframe goes from 9219 to 1298 rows
    filt = (x['popularity'] > 2) & (x['runtime'] > 60) & (x['vote_average'] >= 6) & (x['vote_count'] > 600)
    x = x.loc[filt]
    return x


# Uncomment the line below if you want a much smaller df: from 46628 to 1298 rows
df = get_smaller_df(df).drop(columns=['runtime'])

# =================  More Set-up =================
# Making sure the information in these col are Python literal structures (strings, numbers, tuples, lists, dicts, booleans, or None)
df['cast'] = df['cast'].apply(literal_eval)
df['crew'] = df['crew'].apply(literal_eval)
df['keywords'] = df['keywords'].apply(literal_eval)

# Appending new cols with the number of cast and crew per movie
df['cast_size'] = df['cast'].apply(lambda x: len(x))
df['crew_size'] = df['crew'].apply(lambda x: len(x))


def find_directors(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
    return np.nan


# Takes the director's name from the crew col's dictionary and appends it to a new col
df['director'] = df['crew'].apply(find_directors)
# Making a list out of the cast
df['cast'] = df['cast'].apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])
# Making a list out of the top/first 3 cast members
df['cast'] = df['cast'].apply(lambda x: x[:3] if len(x) >= 3 else x)
# Making a list out of the keywords (names without id)
df['keywords'] = df['keywords'].apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])
# Making the cast-members' names lowercase, removing the spaces, and casting them as strings
df['cast'] = df['cast'].apply(lambda x: [str.lower(i.replace(" ", "")) for i in x])
# Making the directors' names lowercase, removing the spaces, and casting them as strings
df['director'] = df['director'].astype('str').apply(lambda x: str.lower(x.replace(" ", "")))

# Making the director col into a list where their name is mentioned twice (to add weight)
df['director'] = df['director'].apply(lambda x: [x, x])

# Making a series/list where I count the frequency of keywords and remove the movies that only show up once
series = df.apply(lambda x: pd.Series(x['keywords']), axis=1).stack().reset_index(level=1, drop=True)
series.name = 'keyword'
series = series.value_counts()
series = series[series > 1]

# SnowballStemmer truncates words to their stem (older->old)
stemmer = SnowballStemmer('english')


def replace_keywords(x):
    words = []
    for i in x:
        if i in series:
            words.append(i)
    return words


# Making the previous series/list replace the 'keywords' col
df['keywords'] = df['keywords'].apply(replace_keywords)
# Change keywords into their stem format
df['keywords'] = df['keywords'].apply(lambda x: [stemmer.stem(i) for i in x])
# Making the keywords' lowercase, removing the spaces, and casting them as strings
df['keywords'] = df['keywords'].apply(lambda x: [str.lower(i.replace(" ", "")) for i in x])

# Create the soup col which is comprised of the col keywords, cast, director, and genres (twice as much keywords and director)
df['soup'] = df['keywords'] + df['cast'] + df['director'] + df['genres'] + df['keywords']
# Turn the list into a long string with ' ' in between each word
df['soup'] = df['soup'].apply(lambda x: ' '.join(x))

# ================= Bag of Words  =================

vectorizer = CountVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0, stop_words='english')
# fit the df: figures out what all the words in the corpus are, and
# assigns numbers or list indices to each of them
# transform the df: takes all the words in the corpus, and
# and figures out how many counts of each word occur
v_zer_matrix = vectorizer.fit_transform(df['soup'])

# Finding the cosine similarity from this vectorized soup
cos_sim = cosine_similarity(v_zer_matrix, v_zer_matrix)

# Setting up a way to easily be able to get the index when given a title
df = df.reset_index()
indices = pd.Series(df.index, index=df['title'])


# ================= WR and Recommender Functions  =================
# Similar to IMDB's original weighted rating formula
# v and R remain the same (v = # of votes of movie; R = ave rating of movie)
# C = mean rating for all movies in list; m = minimum votes required to be recommended
def weighted_rating(x, m, C):
    v = x['vote_count']
    R = x['vote_average']
    return (v / (v + m) * R) + (m / (m + v) * C)


def recommender(movie_title):
    # Provides the index for movie_title
    index = indices[movie_title]
    # Makes a numbered/indexed list for the cosine similarities of that index
    cos_sim_list = list(enumerate(cos_sim[index]))
    # List is sorted so the most similar movie is on top (itself)
    cos_sim_list = sorted(cos_sim_list, key=lambda x: x[1], reverse=True)
    # Removing itself and keeping a limited number of the most similar movies
    # cos_sim_list = cos_sim_list[1:26]
    cos_sim_list = cos_sim_list[1:51]
    # Sheds the cosine similarity and keeps the indices
    movie_indices = [i[0] for i in cos_sim_list]

    # Making a list of movies with the previous indices and the col's listed below
    movies = df.iloc[movie_indices][['title', 'vote_count', 'vote_average', 'year']]
    # Only including vote counts and averages that aren't null
    vote_counts = movies[movies['vote_count'].notnull()]['vote_count'].astype('float')
    vote_averages = movies[movies['vote_average'].notnull()]['vote_average'].astype('float')

    # Finding the mean rating for all movies in this list
    C = vote_averages.mean()
    # Finding the minimum votes required to be recommended
    m = round(vote_counts.quantile(0.70))

    # Only including the movies that meet the criteria
    final_list = movies[
        (movies['vote_count'] >= m) & (movies['vote_count'].notnull()) & (movies['vote_average'].notnull())]
    final_list['vote_count'] = final_list['vote_count'].astype('float')
    final_list['vote_average'] = final_list['vote_average'].astype('float')
    # Making a new col with the weighted ratings (calling the function for each movie)
    final_list['w_r'] = final_list.apply(weighted_rating, args=(m, C), axis=1)
    # Sorting in descending order, then limiting the number of movies to output
    final_list = final_list.sort_values('w_r', ascending=False)
    final_list = movies['title']
    final_list = final_list[0:10]
    return final_list.to_string(index=False)
