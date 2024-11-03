from flask import Flask
import random
import datetime

app = Flask('__name__')

cars_list = ['Chevrolet', 'Renault', 'Ford', 'Lada', 'Mazda']
cats_list = ['Корниш-рекс', 'Русская голубая', 'Шотландская вислоухая', 'Мейн-кун', 'Манчкин']

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

if __name__ == '__main__':
    app.run(debug=True)