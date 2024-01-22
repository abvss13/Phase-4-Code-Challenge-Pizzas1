from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk":"fk_%(table_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id=db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    address= db.Column(db.String)

    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant')

    def __repr__(self):
        return f'<Restaurant {self.name} {self.address}>'


class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id=db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    ingredients= db.Column(db.String)

    restaurant_pizzas = db.relationship('RestaurantPizza', backref='pizza')

    def __repr__(self):
        return f'<Pizza {self.name} {self.ingredients}>'


class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    serialize_rules = ('-restaurant.restaurant_pizzas', '-pizza.restaurant_pizzas',)

    id=db.Column(db.Integer, primary_key=True)
    price= db.Column(db.String)
    pizza_id= db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id= db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    
    @validates('price')
    def validate_price(self, key, value):
        if not (1 <= value <= 30):
            raise ValueError("Price must be between 1 and 30.")
        return value

    def __repr__(self):
        return f'<RestaurantPizza {self.id} pizza={self.pizza_id} restaurant={self.restaurant_id} price={self.price}>'



