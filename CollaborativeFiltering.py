import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

# Import Movie Data from CSV file
ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')
print(ratings)