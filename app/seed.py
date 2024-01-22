from faker import Faker
from random import randint, choice
from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

fake = Faker()

with app.app_context():
    # Clear existing data
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    # Seeding the restaurants
    restaurants = []
    for _ in range(20):
        restaurant = Restaurant(
            name=fake.company(),
            address=fake.address()
        )
        restaurants.append(restaurant)

    db.session.add_all(restaurants)
    db.session.commit()

    # Seeding the pizzas
    pizzas = []
    pizza_names = [
        'Classic Margherita', 'Pepperoni Lover\'s', 'Vegetarian Delight', 'Supreme Feast',
        'Mushroom Madness', 'BBQ Ranch Chicken', 'Spicy Sausage', 'Savory Seafood', 'Pesto Perfection',
        'Buffalo Ranch', 'Ultimate Veggie', 'Quattro Formaggi', 'Carnivore\'s Dream',
        'Plant-Based Bliss', 'Garlic White Pizza', 'Taco Fiesta', 'Greek Mediterranean', 'Sweet and Spicy BBQ',
        'Bacon & Mushroom Deluxe', 'Spinach and Artichoke'
    ]

    # List of pizza ingredients
    pizza_ingredients = [
        'Dough, Tomato Sauce, Mozzarella Cheese',
        'Dough, Tomato Sauce, Pepperoni, Mozzarella Cheese',
        'Dough, Tomato Sauce, Ham, Pineapple, Mozzarella Cheese',
        'Dough, Tomato Sauce, Mushrooms, Bell Peppers, Onions, Black Olives, Mozzarella Cheese',
        'Dough, Tomato Sauce, Pepperoni, Sausage, Mushrooms, Bell Peppers, Onions, Mozzarella Cheese',
        'Dough, Tomato Sauce, Mushrooms, Mozzarella Cheese',
        'Dough, BBQ Sauce, Grilled Chicken, Red Onions, Cilantro, Mozzarella Cheese',
        'Dough, Tomato Sauce, Sausage, Pepperoni, Bacon, Ground Beef, Mozzarella Cheese',
        'Dough, Tomato Sauce, Shrimp, Calamari, Clams, Mozzarella Cheese',
        'Dough, Pesto Sauce, Cherry Tomatoes, Fresh Basil, Mozzarella Cheese',
        'Dough, Buffalo Sauce, Grilled Chicken, Red Onions, Ranch Drizzle, Mozzarella Cheese',
        'Dough, Tomato Sauce, Mushrooms, Bell Peppers, Spinach, Red Onions, Black Olives, Mozzarella Cheese',
        'Dough, Alfredo Sauce, Ricotta Cheese, Parmesan Cheese, Mozzarella Cheese',
        'Dough, Tomato Sauce, Pepperoni, Sausage, Bacon, Ham, Mozzarella Cheese',
        'Dough, Vegan Tomato Sauce, Vegan Cheese, Mixed Vegetables',
        'Dough, Garlic Alfredo Sauce, Spinach, Artichoke Hearts, Mozzarella Cheese',
        'Dough, Taco Sauce, Seasoned Ground Beef, Tomatoes, Lettuce, Cheddar Cheese, Sour Cream',
        'Dough, Tzatziki Sauce, Gyro Meat, Red Onions, Tomatoes, Feta Cheese, Kalamata Olives',
        'Dough, BBQ Sauce, Grilled Chicken, Bacon, Red Onions, Pineapple, Mozzarella Cheese',
        'Dough, BBQ Sauce, Ground Beef, Bacon, Red Onions, Pickles, Cheddar Cheese',
        'Dough, Creamy Garlic Sauce, Spinach, Artichoke Hearts, Mozzarella Cheese'
    ]

     # Selecting unique pizza names
    unique_pizza_names = list(set(pizza_names))

    for name in unique_pizza_names:
        ingredients = choice(pizza_ingredients)  # Randomly select ingredients
        pizza = Pizza(name=name, ingredients=ingredients)
        pizzas.append(pizza)

    db.session.add_all(pizzas)
    db.session.commit()

# Seeding restaurant pizzas
    restaurant_pizzas = []
    for _ in range(20):
        price = randint(1, 30)
        pizza = choice(pizzas)
        restaurant = choice(restaurants)
        random_pizza = RestaurantPizza(price=price, pizza=pizza, restaurant=restaurant)
        restaurant_pizzas.append(random_pizza)

    db.session.add_all(restaurant_pizzas)
    db.session.commit()