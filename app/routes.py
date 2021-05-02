from flask import Blueprint
from app.models.planet import Planet
from flask import request, Blueprint, make_response, jsonify
from app import db

# planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
solar_world_development_bp = Blueprint("Planet", __name__, url_prefix="/planets")

# @app.route("/", methods=["GET"])
# def test():
#     print("hello world")

# ENDPOINT 1 # Together these arguments ("/create-a-planet", methods=["POST"]) define what type of request will be routed to this function. The first argument defines the path (or URL) of the request and the second argument defines a list of HTTP methods (i.e. GET, PUT, POST) the request could have.
# 
@solar_world_development_bp.route("/create-a-planet", methods=["POST"])
def create_a_planet():
    request_body = request.get_json()
    new_planet = Planet(title=request_body["name"],
                    description=request_body["description"],
                    color=request_body["color"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

# ENDPOINT 2
@solar_world_development_bp.route("/retrieve-all-planets", methods=["GET"]) # 404 in Postman
def retrieve_all_planets():
    planets = Planet.query.all() 
    return jsonify(planets)

    return jsonify(p.to_dict() for p in planets)

# ENDPOINT 3 # jsonify - flask handlesI
@solar_world_development_bp.route("/retrieve-one-planet/<planet_title>", methods=["GET"])
def retrieve_one_planets(planet_title):
    planet = Planet.query.filter_by(title=planet_title).first()
    return jsonify(planet)