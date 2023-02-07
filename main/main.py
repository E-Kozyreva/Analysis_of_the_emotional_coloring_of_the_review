import json
import numpy as np
import user
import Preprocessing
import Vectorization
import KDTree_vec
import Mood_review

user_rev = user.get_data()

with open("reviews_data.json", "r") as read_file:
    load_reviews = json.load(read_file)

reviews = []
reviews += load_reviews['good']
reviews += load_reviews['bad']
reviews += load_reviews['neutral']

del_symb_rev = Preprocessing.delete_symbols(reviews)
lower_rev = Preprocessing.lower_review(del_symb_rev)
Vectorization.vectorization_reviews(lower_rev)


with open("vectorized.json", "r") as read_file:
    load_data = json.load(read_file)

vec_reviews = []
vec_reviews += load_data["good"]
vec_reviews += load_data["bad"]
vec_reviews += load_data["neutral"]
vec_reviews = np.array(vec_reviews)

similar_rev = KDTree_vec.find_similar(vec_reviews, user_rev)
similar_vec = [vec_reviews[i].tolist() for i in similar_rev]

mood_rev = Mood_review.get_mood(similar_vec, load_data["good"], load_data["bad"], load_data["neutral"])

print(mood_rev)
