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
