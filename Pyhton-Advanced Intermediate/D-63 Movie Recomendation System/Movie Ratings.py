import pandas as pd
import os

def load_dataset(file_path):
    df = pd.read_csv(file_path)
    return df 
def calculate_cosine_similarity(ratings_matrix):
    user_similarity = ratings_matrix.corr(method="cosine")
    return user_similarity

file_path = os.path.join(os.path.dirname(__file__), "movie_ratings.csv")

ratings = load_dataset(file_path)
print(ratings.head())

ratings_matrix = ratings.pivot_table(index="user", columns="movie", values="rating")
print(ratings_matrix)
def compute_reccommendation(user_id, ratings):
    user_ratings = ratings[ratings["user"] == user_id]
    if user_ratings.empty:
        return "No ratings found for this user."
    
    # Compute average rating for each movie
    movie_avg_ratings = ratings.groupby("movie")["rating"].mean()
    #Sort movies by average rating
    movie_avg_ratings = movie_avg_ratings.sort_values(ascending=False)
    return movie_avg_ratings[:10]

print(compute_reccommendation(1, ratings))
    