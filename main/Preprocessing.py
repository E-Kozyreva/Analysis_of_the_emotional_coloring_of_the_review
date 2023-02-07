import re
from nltk.corpus import stopwords


def delete_symbols(review): 
    print("Удаляю ненужные символы в данных...")
    new_review = []
    for word in review:
        reg_sumbols = re.sub('[^\w\s]+|[\d]+', ' ', word)
        reg_eng_symbols = re.sub('[a-zA-Z\s]+', ' ', reg_sumbols)
        new_review.append(reg_eng_symbols.split())
    return new_review


def delete_stop_words(review_words): 
    stop_words = list(stopwords.words('russian'))
    deleted_stop_words = []
    for w in review_words:
        word = w.lower()
        if word not in stop_words and word != "\n":
            deleted_stop_words.append(word)
    return deleted_stop_words


def lower_review(review_words): 
    print("Перевожу данные в нижний регистр...")
    lower_reviews = []
    for rev in review_words:
        deleted_stop_words = delete_stop_words(rev)
        lower_reviews.append(deleted_stop_words)
    return lower_reviews