import requests
import json


def test_create_new_movie_invalid_fail():
    url = "http://localhost:3000/api/movies"

    payload = json.dumps({"title": "cat", "year": 2002})
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, data=payload)

    assert response.status_code == 401
