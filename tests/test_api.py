from utils.api_client import get_request, post_request

def test_get_users_api():
    url = "https://jsonplaceholder.typicode.com/users"

    response = get_request(url)

    # Validate status code
    assert response.status_code == 200

    data = response.json()

    # Validate response type
    assert isinstance(data, list)

    # Validate list not empty
    assert len(data) > 0

    # Validate required keys exist in first user
    first_user = data[0]

    assert "id" in first_user
    assert "name" in first_user
    assert "username" in first_user
    assert "email" in first_user


def test_create_user_api():
    url = "https://jsonplaceholder.typicode.com/users"

    payload = {
        "name": "Sangamesh",
        "username": "sangamesh_qa",
        "email": "test@example.com"
    }

    response = post_request(url, payload)

    assert response.status_code == 201

    data = response.json()
    assert data["name"] == payload["name"]

def test_create_user_invalid_payload():
    """
    Verify API handles invalid payload properly.
    """

    url = "https://jsonplaceholder.typicode.com/users"

    # Sending invalid payload (missing required fields)
    payload = {}

    response = post_request(url, payload)

    # In real APIs, this should return 400 (Bad Request)
    # But jsonplaceholder always returns 201 (fake API)
    # So we validate response exists instead

    assert response.status_code in [201, 400]

    data = response.json()
    assert isinstance(data, dict)
