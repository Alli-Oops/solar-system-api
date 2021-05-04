import pytest
from app import create_app
from app import db
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()



@pytest.fixture
def two_saved_planets(app):
    # Arrange
    Saturn_planet = Planet(name="Saturn",
                      description="Round",
                      color="Pink" )
    Pluto_planet = Planet(name="Pluto",
                         description="Rocky",
                         color="Blue")

    db.session.add_all([Saturn_planet, Pluto_planet])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()

    
