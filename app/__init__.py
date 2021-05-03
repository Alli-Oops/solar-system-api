from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy() 
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'

    from .routes import solar_world_development_bp
    app.register_blueprint(solar_world_development_bp)
    

    db.init_app(app)
    migrate.init_app(app, db)
    

    return app

#if __name__ == "__main__":
#    create_app()

