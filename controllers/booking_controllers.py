from flask import render_template, request
from models.booking_models import get_car_list, update_booking_dates, get_car_details, store_customer_data


def search():
    pickup_date = request.form['pickup']
    dropoff_date = request.form['dropoff']
    
    car_list = get_car_list()
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

def final_booking():
    car_id = request.args.get('car_id')
    pickup_date = request.args.get('pickup')
    dropoff_date = request.args.get('dropoff')
    return render_template('final_booking.html', car_id=car_id, pickup_date=pickup_date, dropoff_date=dropoff_date)


def book_car():
    car_id = request.form['car_id']
    pickup_date = request.form['pickup']
    dropoff_date = request.form['dropoff']
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    customer_data = {
        'car_id': car_id,
        'pickup_date': pickup_date,
        'dropoff_date': dropoff_date,
        'name': name,
        'email': email,
        'phone': phone
    }

    if store_customer_data(customer_data):
        if update_booking_dates(car_id, pickup_date, dropoff_date):
            return "Car booked successfully!"
    return "Car Booked succesfully"