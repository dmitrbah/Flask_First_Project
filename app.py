from flask import Flask

app = Flask('__name__')

cars_list = ['Chevrolet', 'Renault', 'Ford', 'Lada']

@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'

@app.route('/cars')
def cars():
    global cars_list
    result = ', '.join(car for car in cars_list)
    return result

if __name__ == '__main__':
    app.run(debug=True)