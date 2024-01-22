# Flask Code Challenge - Pizza Restaurants

This is a Flask-based API that allows one to manage pizza restaurants and their associated pizzas. You can perform various operations, such as listing all restaurants, retrieving a specific restaurant and deleting restaurants, listing all pizzas, and creating restaurant pizzas.

# Table of Contents
1. Prerequisites
2. Getting started
3. Usage
4. Database Models
5. API endpoints
6. License
7. Author


 # Prerequisites
- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate

# Getting started
1. Clone this repository to your local machine
2. Navigate to the project directory.
3. Create a virtual environment:

       pipenv install
4. Activate the virtual environment:

       pipenv shell
5. Initialize the SQLite database:

       flask db init
6. Apply the initial migration:

       flask db migrate
7. Upgrade the database:

       flask db upgrade

# Usage
To start the Flask application run:

     flask run

# Database Models

This code challenge includes three database models:

- **Restaurant**: Represents a pizza restaurant.
- **Pizza**: Represents a type of pizza.
- **RestaurantPizza**: Represents the relationship between a restaurant and a pizza, including the price.     

# API Endpoints

The API provides the following routes to interact with the models:

- **GET /restaurants**: List all restaurants.

- **GET /restaurants/int:id**: Retrieve a specific restaurant by ID. Returns detailed information about the restaurant and the associated pizzas.

- **DELETE /restaurants/int:id**: Delete a specific restaurant by ID. Deletes the restaurant and any associated restaurant pizzas.

- **GET /pizzas**: List all pizzas

- **POST /restaurant_pizzas**: Create a new restaurant pizza. Associates an existing pizza with an existing restaurant and sets the price.

# License

This project is licensed under the MIT License.

# Author
Daniel Mararo (Software Engineer)