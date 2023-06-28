import requests
import pandas as pd

def get_car_list():
    response = requests.get('https://64954062b08e17c91791ccc9.mockapi.io/car_models')
    car_list = response.json()
    return car_list

def get_car_details(car_id):
    response = requests.get(f'https://64954062b08e17c91791ccc9.mockapi.io/car_models/{car_id}')
    car = response.json()
    return car

def update_booking_dates(car_id, pickup_date, dropoff_date):
    car = get_car_details(car_id)
    booking_dates = car.get('booking_dates', [])
    dates_between = pd.date_range(start=pickup_date, end=dropoff_date).strftime('%Y-%m-%d').tolist()
    booking_dates.extend(dates_between)
    response = requests.put(
        f'https://64954062b08e17c91791ccc9.mockapi.io/car_models/{car_id}',
        json={'booking_dates': booking_dates}
    )
    return response.status_code == 200

def store_customer_data(customer_data):
    response = requests.post('https://64954062b08e17c91791ccc9.mockapi.io/customer_data', data=customer_data)
    return response.status_code == 200