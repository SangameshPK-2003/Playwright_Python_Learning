import requests


def test_get_users_api():
    """
    Verify users API returns status 200
    and contains expected data.
    """

    url = "https://reqres.in/api/users?page=2"

    # Add headers to avoid 403 block
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    # Status code validation
    assert response.status_code == 200

    # JSON body validation
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0
