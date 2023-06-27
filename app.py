import pandas as pd
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
    car_list = response.json()

    available_cars = []
    for car in car_list:
        if car.get('booking_dates'):
            already_booked = False
            for booked_date in car['booking_dates']:
                if pickup_date <= booked_date <= dropoff_date:
                    already_booked = True
                    break
            if already_booked:
                continue
        available_cars.append(car)

    return render_template('results.html', cars=available_cars)

@app.route('/final_booking')
def final_booking():
    car_id = request.args.get('car_id')
    pickup_date = request.args.get('pickup')
    dropoff_date = request.args.get('dropoff')

    return render_template('final_booking.html', car_id=car_id, pickup_date=pickup_date, dropoff_date=dropoff_date)

@app.route('/book', methods=['POST'])
def book_car():


    car_id = request.form['car_id']


    pickup_date = request.form['pickup']
    dropoff_date = request.form['dropoff']
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    # Store the customer details in Mock API
    customer_data = {
        'car_id': car_id,
        'pickup_date': pickup_date,
        'dropoff_date': dropoff_date,
        'name': name,
        'email': email,
        'phone': phone
    }
    response = requests.post('https://64954062b08e17c91791ccc9.mockapi.io/customer_data', data=customer_data)


    # Retrieve the car details from the Mock API using car_id
    car_response = requests.get(f'https://64954062b08e17c91791ccc9.mockapi.io/car_models/{car_id}')
    car = car_response.json()

    # Update the booking dates for the car
    pickup_date = request.form['pickup']
    dropoff_date = request.form['dropoff']
    booking_dates = car.get('booking_dates', [])

    # Generate a list of dates between the pickup and drop-off dates
    dates_between = pd.date_range(start=pickup_date, end=dropoff_date).strftime('%Y-%m-%d').tolist()
    booking_dates.extend(dates_between)

    # Send a PUT request to update the booking dates
    update_response = requests.put(
        f'https://64954062b08e17c91791ccc9.mockapi.io/car_models/{car_id}',
        json={'booking_dates': booking_dates}
    )

    if update_response.status_code == 200:
        return "Car booked successfully!"
    else:
        return "Failed to book the car. Please try again."


if __name__ == '__main__':
    app.run()
