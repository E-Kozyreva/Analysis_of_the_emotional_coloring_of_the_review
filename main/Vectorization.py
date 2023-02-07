import json
import fasttext

ft = fasttext.load_model('cc.ru.300.bin')


def get_vector(review):
    sentence = "".join(s + " " for s in review)
    sentence_vector = ft.get_sentence_vector(sentence)
    return sentence_vector


def vectorization_reviews(lower_reviews):
    print("Векторизую полученные данные...")
    with open("reviews_data.json", "r") as read_file:
        reviews = json.load(read_file)
    for i in range(1000):
        reviews['good'][i] = get_vector(lower_reviews[i]).tolist()
    for i in range(1000):
        reviews['bad'][i] = get_vector(lower_reviews[i + 1000]).tolist()
    for i in range(1000):
        reviews['neutral'][i] = get_vector(lower_reviews[i + 2000]).tolist()
    with open('vectorized.json', 'w') as outfile:
        json.dump(reviews, outfile)
    print("Загружаю вектора в отдельный файл...")