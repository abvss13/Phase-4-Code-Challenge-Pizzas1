from flask import Flask,jsonify, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db,Restaurant,Pizza,Restaurant_Pizza
from flask_cors import CORS

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.json.compact = False

migrate = Migrate(app,db)
db.init_app(app)
CORS(app)
api = Api(app)

class Home(Resource):
    def get(self):
        return 'Index for Pizza-Restaurant API'
api.add_resource(Home, '/')


class Restaurants(Resource):
    def get(self):
        restaurants = []
        for restaurant in Restaurant.query.all():
            restaurant_dict={
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            }
            restaurants.append(restaurant_dict)
        response = make_response(
            jsonify(restaurants),200
        )
        response.headers["Content-Type"] = "application/json"
        return response

api.add_resource(Restaurants, '/restaurants')

class RestaurantByID(Resource):
    def get(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
          restaurant_dict = restaurant.to_dict()
          response = make_response(
            jsonify(restaurant_dict),200
          )
          return response
        else:
            response = make_response(
                jsonify({"error": "Restaurant not found"})
            )
            return response
    def delete(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()
            return make_response("", 204)
        else :
            response =make_response(
                jsonify({"error": "Restaurant not found"}, 404)
            )
            return response
api.add_resource(RestaurantByID, '/restaurants/<int:id>')
class Pizzas(Resource):
    def get(self):
        pizzas=[]
        for pizza in Pizza.query.all():
            pizza_dict={
                "id":pizza.id,
                "name":pizza.name,
                "ingredients":pizza.ingredients
            }
            pizzas.append(pizza_dict)
        response = make_response(
            jsonify(pizzas),200
        )
        return response
api.add_resource(Pizzas,'/pizzas')

class PizzaById(Resource):
    def get(self, pizza_id):
        pizza = Pizza.query.get(pizza_id)
        if pizza:
            pizza_dict = {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            }
            response = make_response(
                jsonify(pizza_dict), 200
            )
        else:
            response = make_response(
                jsonify({"error": "Pizza not found"}), 404
            )
        return response
api.add_resource(PizzaById, '/pizzas/<int:pizza_id>')


class RestaurantPizza(Resource):
    def post(self):
        try:
          data = request.get_json()
          new_data = Restaurant_Pizza(
            price = data.get("price"),
            pizza_id = data.get("pizza_id"),
            restaurant_id = data.get("restaurant_id")
           )
          db.session.add(new_data)
          db.session.commit()
          record_dict = new_data.to_dict()
          response = make_response(
            jsonify(record_dict),200
          )
          return response
        except Exception as e:
          response =make_response(
                jsonify({"error": "validation errors"}, 500)
            )
          return response 
api.add_resource(RestaurantPizza,'/restaurant_pizzas')

if __name__== '__main__':
    app.run(debug=True,port=5555)
