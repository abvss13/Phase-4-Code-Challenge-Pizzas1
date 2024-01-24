# Pizza Restaurant App

This is a web application for managing pizza restaurants, pizzas, and their prices.
# Frontend link 
https://65b0db59a7302c6629c3b754--clever-llama-0d503d.netlify.app/
# Backend link
https://pizza-restaurant-buse.onrender.com/


## Introduction

This web application provides a platform to manage pizza restaurants and their menus. It allows users to view restaurants, pizzas, and their prices, as well as create new entries.

## Features

- View a list of restaurants
- View details of a specific restaurant, including associated pizzas
- Delete a restaurant and its associated pizzas
- View a list of pizzas
- Create a new restaurant-pizza association with a specified price

## Technologies

- Flask (Python web framework)
- SQLAlchemy (SQL toolkit for Python)
- React (JavaScript library for building user interfaces)
- React Router (Declarative routing for React.js)


## Getting Started

# Prerequisites

- Python
- Node.js
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd pizza-restaurant-app
2. Set up the Python environment:
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
3. Set up the frontend:
    cd frontend
    npm install

### Models
You need to create the following relationships:
- A `Restaurant` has many `Pizza`s through `RestaurantPizza`
- A `Pizza` has many `Restaurant`s through `RestaurantPizza`
- A `RestaurantPizza` belongs to a `Restaurant` and belongs to a `Pizza`
Validations
Add validations to the `RestaurantPizza` model:
- must have a `price` between 1 and 30
Routes
Set up the following routes. Make sure to return JSON data in the format specified along with the appropriate HTTP verb.
 

# GET /restaurants:
Return JSON data in the format below:
```
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
``` 
# GET /restaurants/:id:
If the `Restaurant` exists, return JSON data in the format below:
```
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
If the `Restaurant` does not exist, return the following JSON data, along with the appropriate HTTP status code:
{
  "error": "Restaurant not found"
}
 

```

# DELETE /restaurants/:id:
If the `Restaurant` exists, it should be removed from the database, along with any `RestaurantPizza`s that are associated with it (a `RestaurantPizza` belongs to a `Restaurant`, so you need to delete the `RestaurantPizza`s before the `Restaurant` can be deleted).
After deleting the `Restaurant`, return an _empty_ response body, along with the appropriate HTTP status code.
If the `Restaurant` does not exist, return the following JSON data, along with the appropriate HTTP status code:
```
{
  "error": "Restaurant not found"
}
```
 

# GET /pizzas:
Return JSON data in the format below:
```
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
```
# POST /restaurant_pizzas:
This route should create a new `RestaurantPizza` that is associated with an existing `Pizza` and `Restaurant`. It should accept an object with the following properties in the body of the request:
```
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
If the `RestaurantPizza` is created successfully, send back a response with the data related to the `Pizza`:
{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}
If the `RestaurantPizza` is **not** created successfully, return the following JSON data, along with the appropriate HTTP status code:
{
  "errors": ["validation errors"]
}```
```


### Usage
1. Run the Flask backend:
    python app.py
2. Run the React frontend:
     Run the React frontend:

### API Endpoints
1. GET /restaurants: Get a list of restaurants.
2. GET /restaurants/:id: Get details of a specific restaurant.
3. DELETE /restaurants/:id: Delete a restaurant and its associated pizzas.
4. GET /pizzas: Get a list of pizzas.
5. POST /restaurant_pizzas: Create a new restaurant-pizza association.

### Author
 Tabitha L

### Licence
  This project is licensed under the MIT License .


