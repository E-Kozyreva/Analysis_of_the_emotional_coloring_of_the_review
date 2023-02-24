# Анализ эмоциональной окраски отзывов с Кинопоиска

## Окружение 
* Python 3.8.0

## Как начать
* `git clone git@github.com:E-Kozyreva/фnalysis_of_the_emotional_coloring_of_the_review.git`
* `cd Analysis_of_the_emotional_coloring_of_the_review`
* `python -m venv venv`
* `venv\Scripts\activate`
* `pip install -r requirements.txt`
* `cd main`
* `dowload model from: https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ru.300.bin.gz`
* `unpacking the model to the "main" folder using 7-zip`
* `unpacking reviews_data.zip`
* `python main.py`

## Результат работы
### Положительный отзыв
![image](https://user-images.githubusercontent.com/83861300/217198191-d0eca70a-ea1e-4148-906c-bfb054abcd9b.png) 

### Отрицательный отзыв
![image](https://user-images.githubusercontent.com/83861300/217198249-39b3e133-b4ab-4b31-95fa-d68a3408bbbc.png)

### Нейтральный отзыв
![image](https://user-images.githubusercontent.com/83861300/217198311-916a074b-f6ab-4e9d-8e5c-a5a8b1638ff4.png)
