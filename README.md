# Car Rental
This is a car rental application built using Flask, a web framework in Python. The app allows users to search for available cars based on their desired pickup and drop-off dates. It retrieves car data from a mock API and checks for available cars within the specified dates. Users can then select a car and proceed to the final booking page, where they provide their personal details like name, email, and phone number. The booking details are stored in another mock API, and the car's booking dates are updated accordingly. The app ensures that cars are not double-booked during the same period. Overall, it provides a simple interface for users to search and book cars for rent.
## :computer: [Click here](https://car-rentals-dx0s.onrender.com/) to see my live project!
## :pencil2: Planning & Problem Solving
- Flow charts of app logic.
  ![Wireframing](https://raw.githubusercontent.com/nabeghamazahir/FinalProject/main/Screenshot%202023-06-28%20at%209.19.55%20pm.png)
- ## :rocket: Cool tech
- Flask
- HTML
- CSS
- Jinja2 Templating Engine
- HTTP Requests
- Mock APIs
- Date Manipulation
These technologies and concepts combined create a functional and interactive car rental web application.
## :scream: Bugs to fix :poop:
- Error Handling
## :sob: Lessons learnt
- Code Organization
- Mock API Usage
## :white_check_mark: Future features
- Rating and Reviews
- Search Filters
- Multi-language Support
  
## :General Approach:
The code provided is a Flask application for a car rental booking system. It consists of several routes and templates for handling different functionalities such as searching for available cars, booking a car, and displaying booking details.

The search function handles the POST request from the search form and checks the availability of cars for the specified pickup and drop-off dates. It retrieves the car list from an external API, filters out the already booked cars for the given dates, and renders the 'results.html' template with the available cars.

The final_booking function handles the GET request when a user selects a car to book. It renders the 'final_booking.html' template with the car details and allows the user to enter their contact information.

The book_car function handles the POST request when the user submits the final booking form. It stores the customer's information in an external API and updates the booking dates for the selected car. It returns a success message if the booking is successful.

## User Stories:
Users can search for available cars by selecting pickup and drop-off dates.
Users can view a list of available cars and their details.
Users can select a car and proceed to the final booking form.
Users can enter their contact information and submit the booking form.
Users receive a confirmation message if the booking is successful.

## Unsolved Issues:
Error handling and validation of user inputs.
Authentication and authorization for secure booking.
Integration with a payment gateway for handling payments




