from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    pickup_date = request.form['pickup']
    dropoff_date = request.form['dropoff']
    return f'Searching for cars from {pickup_date} to {dropoff_date}'

if __name__ == '__main__':
    app.run()
