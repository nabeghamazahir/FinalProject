from flask import Flask, render_template
from routes.booking_routes import booking_routes

app = Flask(__name__)
app.register_blueprint(booking_routes, url_prefix = '/booking')

@app.route('/')
def welcome():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()