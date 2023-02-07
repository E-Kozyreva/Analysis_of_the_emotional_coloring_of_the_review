import numpy as np

def get_mood(similar_vec, good, bad, neutral):
    good_rev, bad_rev, neutral_rev = 0, 0, 0

    for rev in similar_vec:
        if rev in good:
            good_rev += 1
        elif rev in bad:
            bad_rev += 1
        elif rev in neutral:
            neutral_rev += 1
    
    if good_rev > bad_rev and good_rev > neutral_rev:
        return "Это положительный отзыв"
    elif bad_rev > good_rev and bad_rev > neutral_rev:
        return "Это отрицательный отзыв"
    elif neutral_rev > good_rev and neutral_rev > bad_rev:
        return "Это нейтральный отзыв"
    else:
        max_mood = max(good_rev, bad_rev, neutral_rev)
        if max_mood == good_rev and max_mood == bad_rev:
            return "Это положительный или отрицательный отзыв"
        elif max_mood == good_rev and max_mood == neutral_rev:
            return "Это положительный или нейтральный отзыв"
        elif max_mood == bad_rev and max_mood == neutral_rev:
            return "Это отрицательный или нейтральный отзыв"