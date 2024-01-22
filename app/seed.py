from server.models import Pizza, Restaurant, RestaurantPizza
from server.app import db, app

pizzas = [{
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
},
{
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
}]

restaurants = [{
    "id": 1,
    "name": "Sottocasa NYC",
    "address": "298 Atlantic Ave, Brooklyn, NY 11201"
},
{
    "id": 2,
    "name": "PizzArte",
    "address": "69 W 55th St, New York, NY 10019"
}]

pizzaRestaurants= [
    {
        "id": 1,
        "price": 5,
        "pizza_id": 1,
        "restaurant_id": 2
    },
    {
        "id": 2,
        "price": 15,
        "pizza_id": 2,
        "restaurant_id": 1
    }
]

with app.app_context():

    db.session.add_all([RestaurantPizza(**rp) for  rp in pizzaRestaurants])
    db.session.commit()

    db.session.add_all([Restaurant(**restaurant) for restaurant in restaurants])
    db.session.commit()

    # db.session.add_all([Pizza(**pizza) for pizza in pizzas])
    # db.session.commit()