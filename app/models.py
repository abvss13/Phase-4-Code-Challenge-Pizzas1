from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    restaurant_pizzas =db.relationship('Restaurant_Pizza', backref='restaurant')

    serialize_rules = ('-restaurant_pizzas.restaurant', '-restaurant_pizzas.pizza.restaurant_pizzas', '-restaurant_pizzas.pizza.restaurant')

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    restaurant_pizzas =db.relationship('Restaurant_Pizza', backref='pizza')

    serialize_rules = ('-restaurant_pizzas.pizza',)

class Restaurant_Pizza(db.Model, SerializerMixin ):
    __tablename__ = 'restaurant_pizzas'
    id = db.Column(db.Integer, primary_key= True)
    price = db.Column(db.Integer)
    pizza_id=db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id=db.Column(db.Integer, db.ForeignKey('restaurants.id'))

    serialize_rules = ('-restaurant.restaurant_pizzas','-pizza.restaurant_pizzas', '-id')
    

    @validates('price')
    def validate_price(self, key, price):
        if not (1<=price<=30):
            raise ValueError("Price must be between 1 and 30.")
        return price
