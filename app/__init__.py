from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy() # 
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'
## 


    db.init_app(app) # allows SQLAlchemy to talk to the database
    migrate.init_app(app, db)


    from .routes import solar_world_development_bp # new line that might fix 404?
    app.register_blueprint(solar_world_development_bp) # new line that might fix 404?
    # use app's pre-defined function register_blueprint() to register the solar_world_development_bp Blueprint.


    return app


