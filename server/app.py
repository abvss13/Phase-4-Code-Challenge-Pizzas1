
from flask import Flask, make_response,jsonify,request
from flask_migrate import Migrate
from flask_restful import Api, Resource,reqparse
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models import db, RestaurantPizza,Pizza,Restaurant
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db,render_as_batch=True)
db.init_app(app)
api = Api(app)
ma = Marshmallow(app)
ma.init_app(app)

class PizzaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Pizza
   

pizza_schema = PizzaSchema()


class RestaurantSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Restaurant
   
restaurant_schema = RestaurantSchema()


class RestaurantPizzaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RestaurantPizza
        fields = ("id", "pizza_id", "restaurant_id")

restaurant_pizza_schema = RestaurantPizzaSchema()

post_args = reqparse.RequestParser(bundle_errors=True)
post_args.add_argument('price', type=float, help='Price of the RestaurantPizza', required=True)
post_args.add_argument('restaurant_id', type=int, help='ID of the associated Restaurant', required=True)
post_args.add_argument('pizza_id', type=int, help='ID of the associated Pizza', required=True)

@app.route('/')
def home():
    return 'welcome to pizza sunset pizza paradise'

class Pizzas(Resource):
    def get(self):
        pizza = Pizza.query.all()
        print(pizza) 
        ravine =pizza_schema.dump(pizza,many = True)
        print (ravine)
        
        response =  make_response(
            jsonify(ravine),
            200
        )
        return response
    
api.add_resource(Pizzas, '/pizzas')

class Restaurants(Resource):
    def get(self):
        restaurant = Restaurant.query.all()
        ravine =restaurant_schema.dump(restaurant,many = True)     

        response =  make_response(
            jsonify(ravine),
            200
        )
        return response
    
api.add_resource(Restaurants, '/restaurant')

class RestaurantById(Resource):
    def get(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()

        if restaurant is None:
            response = make_response(
                jsonify({"error":"Restaurant not found"}),
                404
            )
            return response
        else:
            pizzas = Pizza.query.join(RestaurantPizza).filter_by(restaurant_id=id).all()
            pizza_list = [pizza_schema.dump(pizza) for pizza in pizzas]
            restaurant_dict = restaurant_schema.dump(restaurant)
            restaurant_dict["pizzas"] = pizza_list

            return restaurant_dict    
            
    def delete(self, id):
        restaurant = Restaurant.query.get(id)

        if restaurant is None:
            response = jsonify({"error": "Restaurant not found"})
            response.status_code = 404
            return response

        RestaurantPizza.query.filter_by(restaurant_id=id).delete()

        db.session.delete(restaurant)
        db.session.commit()

        return {"message": "Restaurant deleted successfully"}, 200


        
api.add_resource(RestaurantById, '/restaurants/<int:id>')

class Restaurant_Pizza(Resource):
    def post(self):
        data = post_args.parse_args()

        # Validate input data
        if not (1 <= data["price"] <= 30):
            response_data = {"errors": ["Price must be between 1 and 30"]}
            return make_response(jsonify(response_data), 400)

        pizza = Pizza.query.get(data["pizza_id"])
        restaurant = Restaurant.query.get(data["restaurant_id"])

        if not (pizza and restaurant):
            response_data = {"errors": ["Invalid Pizza or Restaurant ID"]}
            return make_response(jsonify(response_data), 400)

        new_restaurant_pizza = RestaurantPizza(
            price=data["price"],
            restaurant_id=data["restaurant_id"],
            pizza_id=data["pizza_id"]
        )

      
        db.session.add(new_restaurant_pizza)
        db.session.commit()

        pizza_data = pizza_schema.dump(pizza)

        return make_response(
            jsonify(pizza_data),
            201
        )


api.add_resource(Restaurant_Pizza, '/new_restaurants')


if __name__ == '__main__':
    app.run(port=5555, debug=True)