import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    pickup_date = request.form['pickup']
    dropoff_date = request.form['dropoff']

    response = requests.get('https://64954062b08e17c91791ccc9.mockapi.io/car_models')

    if response.status_code == 200:

        car_models = response.json()

    
        available_cars = []
        for car in car_models:
            if pickup_date in car['available_dates'] and dropoff_date in car['available_dates']:
                available_cars.append(car)

        return render_template('results.html', cars=available_cars)
    else:
        return 'Error occurred while fetching car data'

if __name__ == '__main__':
    app.run()
