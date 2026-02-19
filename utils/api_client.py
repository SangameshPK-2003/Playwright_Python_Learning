import requests


def get_request(url):
    """
    Reusable GET request function.
    """
    return requests.get(url)


def post_request(url, payload):
    """
    Reusable POST request function.
    """
    return requests.post(url, json=payload)
