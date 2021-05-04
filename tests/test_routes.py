def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets/retrieve-all-planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/retrieve-one-planet/Saturn")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["name"] == "Saturn"


def test_get_one_planet_with_no_records(client):
    # Act
    response = client.get("/planets/retrieve-one-planet/Saturn")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404

def test_retrieve_all_planets_with_records(client, two_saved_planets):
    # Act
    response = client.get("/planets/retrieve-all-planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200 
    assert response_body[0]["name"] == "Saturn"
    assert response_body[1]["name"] == "Pluto"

def test_create_a_planet(client):
    # Act
    response = client.post("/planets/create-a-planet", json={ 
        "name": "Saturn",
        "description": "Round",
        "color": "Pink"
    })
    #response_body = magic_box_that_makes_everything_perfect()

    # Assert
    assert response.status_code == 201
    #assert response_body = 