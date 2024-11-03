from idlelib.iomenu import encoding

from flask import Flask
import random
import datetime
import os

app = Flask('__name__')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

cars_list = ['Chevrolet', 'Renault', 'Ford', 'Lada', 'Mazda']
cats_list = ['Корниш-рекс', 'Русская голубая', 'Шотландская вислоухая', 'Мейн-кун', 'Манчкин']
words_list = list()

@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'

@app.route('/cars')
def cars():
    global cars_list
    result = ', '.join(car for car in cars_list)
    return result

@app.route('/cats')
def cats():
    global cats_list
    result = random.choice(cats_list)
    return result

@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.datetime.now()
    return f'Точное время {current_time}'

@app.route('/get_time/future')
def get_time_future():
    current_time = datetime.datetime.now()
    delta = datetime.timedelta(hours=1)
    future_time = current_time + delta
    return f'Точное время через час будет {future_time}'

def gen_words_list(file):
    with open(file, 'r', encoding='utf-8') as f:
        global words_list
        words_list = [word.strip() for line in f for word in line.split()]
    for i, word in enumerate(words_list):
        words_list[i] = ''.join(e for e in word if e.isalnum())
    words_list = [value for value in words_list if value]

@app.route('/get_random_word')
def get_random_word():
    global words_list
    result = random.choice(words_list)
    return result

if __name__ == '__main__':
    gen_words_list(BOOK_FILE)
    app.run(debug=True)