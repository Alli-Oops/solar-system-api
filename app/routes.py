from app import db
from flask import Blueprint, request, make_response, jsonify
from app.models.planet import Planet 


solar_world_development_bp = Blueprint("Planet", __name__, url_prefix="/planets")


@solar_world_development_bp.route("/retrieve-all-planets", methods=["GET"])
def retrieve_all_planets():
  planets = Planet.query.all() 


  return jsonify(planets)


@solar_world_development_bp.route("/retrieve-one-planet/<planet_name>", methods=["GET", "PUT", "DELETE"])
def retrieve_one_planet(planet_name):
    planet = Planet.query.filter_by(name = planet_name).first()
    
    if request.method == "GET": 
        return jsonify(planet)
    elif request.method == "PUT": 
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data ["description"]
        planet.color = form_data ["color"]

        db.session.commit()

        return make_response (f"Planet #{planet.id} sucessfully updated, 201")

    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Planet #{planet.id} successfully deleted, 200")


    


@solar_world_development_bp.route("/create-a-planet", methods=["POST"])
def create_a_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    color=request_body["color"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

    