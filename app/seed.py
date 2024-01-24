# seed.py
from random import randint, choice
from app import app
from models import db, Restaurant, Pizza, Restaurant_Pizza

print("🍕 Seeding restaurants...")
restaurants_data = [
    {"name": "Pizzeria Uno", "address": "123 Main St"},
    {"name": "Pizza Hut", "address": "456 Oak St"},
    {"name": "Domino's Pizza", "address": "789 Pine St"},
    {"name": "Little Caesars", "address": "101 Elm St"},
    {"name": "Papa John's", "address": "202 Cedar St"}
]

with app.app_context():
    for restaurant_info in restaurants_data:
        restaurant = Restaurant(**restaurant_info)
        db.session.add(restaurant)

    db.session.commit()

print("🍕 Seeding pizzas...")
pizzas_data = [
    {"name": "Margherita", "ingredients": "Dough ,Tomato, Mozzarella, Basil"},
    {"name": "Pepperoni", "ingredients": "Dough, Tomato, Mozzarella, Pepperoni"},
    {"name": "Vegetarian", "ingredients": "Dough, Tomato, Mozzarella, Bell Peppers, Olives"},
    {"name": "Hawaiian", "ingredients": "Dough, Tomato, Mozzarella, Ham, Pineapple"},
    {"name": "BBQ Chicken", "ingredients": "Dough, BBQ Sauce, Mozzarella, Chicken, Red Onion"}
]

with app.app_context():
    for pizza_info in pizzas_data:
        pizza = Pizza(**pizza_info)
        db.session.add(pizza)

    db.session.commit()

print("🍕 Linking pizzas to restaurants...")
with app.app_context():
    for restaurant in Restaurant.query.all():
        for _ in range(randint(1, 3)):
            pizza = Pizza.query.get(randint(1, Pizza.query.count()))
            price = randint(5, 25)

            restaurant_pizza = Restaurant_Pizza(restaurant=restaurant, pizza=pizza, price=price)
            db.session.add(restaurant_pizza)

    db.session.commit()

print("🍕 Done seeding!")
