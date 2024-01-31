import requests


def test_get_movie_list_invalid_fail():
    url = "http://localhost:3000/api/movies"

    payload = ""
    headers = {}

    response = requests.get(url, headers=headers, data=payload)

    assert response.status_code == 401
