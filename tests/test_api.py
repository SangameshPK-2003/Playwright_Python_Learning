import requests


def test_get_users_api():
    """
    Verify users API returns status 200
    and contains expected data.
    """

    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    # Status code validation
    assert response.status_code == 200

    # JSON body validation
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_create_user_api():
    """
    Verify user creation via POST API.
    """

    url = "https://jsonplaceholder.typicode.com/users"

    payload = {
        "name": "Sangamesh",
        "username": "sangamesh_qa",
        "email": "test@example.com"
    }

    response = requests.post(url, json=payload)

    # Status code validation (201 = created)
    assert response.status_code == 201

    # Response body validation
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]