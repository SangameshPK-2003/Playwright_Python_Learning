from utils.api_client import get_request, post_request

def test_get_users_api():
    url = "https://jsonplaceholder.typicode.com/users"

    response = get_request(url)

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


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
