from flask import Blueprint
from controllers.booking_controllers import search, final_booking, book_car
booking_routes = Blueprint('booking_bp', __name__)

booking_routes.route('/search', methods=['POST'])(search)
booking_routes.route('/final_booking')(final_booking)
booking_routes.route('/book', methods=['POST'])(book_car)