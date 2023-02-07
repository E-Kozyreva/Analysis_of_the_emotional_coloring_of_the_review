import re
import numpy as np
import Preprocessing
import Vectorization

def get_data():
    print()
    review = input("Введи свой отзыв сюда: ")
    print()
    print("Удаляю ненужные символы в отзыве...")
    reg_sumbols = re.sub('[^\w\s]+|[\d]+', ' ', review)
    reg_eng_symbols = re.sub('[a-zA-Z\s]+', ' ', reg_sumbols)
    new_user_review = reg_eng_symbols.split()
    print("Перевожу отзыв в нижний регистр...")    
    lower_user_review = []
    deleted_stop_words = Preprocessing.delete_stop_words(new_user_review)
    lower_user_review.append(deleted_stop_words)
    print("Векторизую отзыв...\n")
    vec_user_review = Vectorization.get_vector(*lower_user_review).tolist()
    print("Перехожу к загрузке данных")
    return np.array(vec_user_review)