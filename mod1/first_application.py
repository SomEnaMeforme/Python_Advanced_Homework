from flask import Flask
import random
from datetime import datetime, timedelta
import os
import re

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/hello_world')
def hello_world() -> str:
    return 'Привет, мир!'


class Cars:
    cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']

    @staticmethod
    @app.route('/cars')
    def get_cars() -> str:
        return ', '.join(Cars.cars)


class Cats:
    cat_breeds = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']

    @staticmethod
    @app.route('/cats')
    def get_random_cat_breed() -> str:
        return random.choice(Cats.cat_breeds)


@app.route('/get_time/now')
def get_time_now() -> str:
    current_time = datetime.now().strftime('%H:%M %d.%m.%Y')
    return f'Точное время: {current_time}'


@app.route('/get_time/future')
def get_time_after_hour() -> str:
    current_time_after_hour = (datetime.now() + timedelta(hours=1)).strftime('%H:%M %d.%m.%Y')
    return f'Точное время через час будет {current_time_after_hour}'


class War_and_peace:
    words = []

    @staticmethod
    @app.route('/get_random_word')
    def get_random_word() -> str:
        txt_len = len(War_and_peace.words)
        if (txt_len == 0):
            War_and_peace.words = War_and_peace.get_words_from_file('war_and_peace.txt')
        return random.choice(War_and_peace.words)

    @staticmethod
    def get_words_from_file(file_name):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        BOOK_FILE = os.path.join(BASE_DIR, file_name)
        with open(BOOK_FILE) as book:
            str = book.read()
            words = re.findall(r'[А-Яа-яЁёa-zA-Z]+', str)
        return words


class Counter:
    visits = 0

    @staticmethod
    @app.route('/counter')
    def counter():
        Counter.visits += 1
        return str(Counter.visits)
