from scipy import spatial


def find_similar(vec_reviews, user_review):
    print("Ищу схожий отзыв для оценки...")
    treee = spatial.KDTree(vec_reviews)
    similar_review = treee.query(user_review, 10)
    print()
    return similar_review[1]
