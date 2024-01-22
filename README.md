
Pizza Restaurant API - Flask Backend


This is a Flask backend API for managing Pizza Restaurants. It provides endpoints to interact with restaurant, pizza, and pizza-restaurant relationship data.

Table of Contents
Models
Validations
Routes
Project Setup
Usage
Project Submission
Contributing
License
Models
Relationships:
A Restaurant has many Pizzas through RestaurantPizza.
A Pizza has many Restaurants through RestaurantPizza.
A RestaurantPizza belongs to a Restaurant and belongs to a Pizza.
Validations:
Add validations to the RestaurantPizza model:

Must have a price between 1 and 30.
Routes
GET /restaurants
Return JSON data containing a list of restaurants:

json
Copy code
[
  {
    "id": 1,
    "name": "Sottocasa NYC",
    "address": "298 Atlantic Ave, Brooklyn, NY 11201"
  },
  {
    "id": 2,
    "name": "PizzArte",
    "address": "69 W 55th St, New York, NY 10019"
  }
]
GET /restaurants/:id
If the Restaurant exists, return JSON data containing details:

json
Copy code
{
  "id": 1,
  "name": "Sottocasa NYC",
  "address": "298 Atlantic Ave, Brooklyn, NY 11201",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}
If the Restaurant does not exist, return:

json
Copy code
{
  "error": "Restaurant not found"
}
DELETE /restaurants/:id
If the Restaurant exists, remove it from the database, along with any associated RestaurantPizzas. After deletion, return an empty response body.

If the Restaurant does not exist, return:

json
Copy code
{
  "error": "Restaurant not found"
}
GET /pizzas
Return JSON data containing a list of pizzas:

json
Copy code
[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]
POST /restaurant_pizzas
Create a new RestaurantPizza associated with an existing Pizza and Restaurant. Accept an object with the following properties in the request body:

json
Copy code
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
If the RestaurantPizza is created successfully, send back a response with the data related to the Pizza:

json
Copy code
{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}
If the RestaurantPizza is not created successfully, return:

json
Copy code
{
  "errors": ["validation errors"]
}
Project Setup
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/pizza-restaurant-api.git
Change into the project directory:

bash
Copy code
cd pizza-restaurant-api
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up your database. Update the config.py file with your database configurations.

Apply database migrations:

bash
Copy code
flask db init
flask db migrate
flask db upgrade
Run the Flask application:

bash
Copy code
flask run
The API should now be running at http://localhost:5000.

Usage
Use the provided routes to interact with the API, e.g., use a tool like curl or Postman to make requests.

Integrate the API with a React frontend for a fully functional application.

Project Submission
Create a private repository on GitHub.

Add your TM as a collaborator for grading and review.

Push your code to the repository.

Submit the link to the repository.

Contributing
If you'd like to contribute to this project, please follow these guidelines:

Fork the repository.

Create a new branch for your feature: git checkout -b feature-name.

Make your changes and commit them: git commit -m 'Add new feature'.

Push to the branch: git push origin feature-name.

Create a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.