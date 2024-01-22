from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Hero, HeroPowers, Power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

@app.route('/')
def home():
    return 'This is the home page'

class HeroResource(Resource):
    def get(self):
        # getting the heroes
        heros = Hero.query.all()

        heroes_list = [{'id': hero.id, 'name': hero.name, 'super_name': hero.super_name} for hero in heros]
        return make_response(jsonify(heroes_list), 200)


class HeroID(Resource):
    def get(self, id):
        hero_one = Hero.query.filter_by(id=id).first()
        if hero_one is None:
            return make_response(jsonify({"error": "Hero not found"}), 404)
        else:
            # getting the powers for that hero
            hero_details = {
                'id': hero_one.id,
                'name': hero_one.name,
                'super_name': hero_one.super_name,
                'powers': []
            }

            for hero_power in hero_one.hero_powers:
                power_info = {
                    'id': hero_power.power.id,
                    'name': hero_power.power.name,
                    'description': hero_power.power.description
                }
                hero_details['powers'].append(power_info)

            return make_response(jsonify(hero_details), 200)


class PowerResource(Resource):
    def get(self):
        powers = Power.query.all()
        powers_list = [{'id': power.id, 'name': power.name, 'description': power.description} for power in powers]

        return make_response(jsonify(powers_list), 200)


class PowerID(Resource):
    def get(self, id):
        power_one = Power.query.filter_by(id=id).first()

        if power_one is None:
            return make_response(jsonify({"error": "Power not found"}), 404)
        else:
            power_details = [{'id': power_one.id, 'name': power_one.name, 'description': power_one.description}]
            return make_response(jsonify(power_details), 200)

    # patch for the power description
    def patch(self, id):
        data = request.get_json()
        power = Power.query.filter_by(id=id).first()

        # checking if the power exists
        if power is None:
            return make_response(jsonify({"error": "Power not found"}), 404)

        # validation for the length of the description
        if len(data["description"]) < 20:
            return jsonify({
                "errors": ["description must be at least 20 characters long"]
            }), 400

        # updating the description
        try:
            power.description = data["description"]
            db.session.commit()

        except Exception as e:
            # If the power is not updated successfully, return an error response
            return jsonify({
                "errors": ["validation errors"]
            }), 400

        new_response = {
            'id': power.id,
            'name': power.name,
            'description': power.description
        }
        return make_response(jsonify(new_response), 200)


# post for a heropower creating new records
class HeroPowersResource(Resource):
    def post(self):
        data = request.get_json()
        strength = data.get('strength')
        hero_id = data.get('hero_id')
        power_id = data.get('power_id')

        # Check if the hero and power exist in the database
        hero = Hero.query.get(hero_id)
        power = Power.query.get(power_id)

        if not hero:
            return make_response(jsonify({"error": "Hero not found"}), 404)

        if not power:
            return make_response(jsonify({"error": "Power not found"}), 404)

        new_heropower = HeroPowers(
            strength=strength,
            hero_id=hero_id,
            power_id=power_id
        )
        db.session.add(new_heropower)
        db.session.commit()

        # returning a response
        response = {
            'id': hero.id,
            'name': hero.name,
            'super_name': hero.super_name,
            'powers': [
                {
                    'id': power.id,
                    'name': power.name,
                    'description': power.description
                }
            ]
        }

        return make_response(jsonify(response), 200)


api.add_resource(HeroResource, '/heroes')
api.add_resource(HeroID, '/heroes/<int:id>')
api.add_resource(PowerResource, '/powers')
api.add_resource(PowerID, '/powers/<int:id>')
api.add_resource(HeroPowersResource, '/hero_powers')

if __name__ == '__main__':
    app.run(port=5555)