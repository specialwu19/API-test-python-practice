import requests
import json
from share_variable import get_variable, add_variable


def test_create_new_movie_valid_pass():
    url = "http://localhost:3000/api/movies"

    payload = json.dumps({"title": "dragon", "year": 2024})

    headers = {
        "Authorization": f'Bearer {get_variable("user_token")}',
        "Content-Type": "application/json",
    }

    response = requests.post(url, headers=headers, data=payload)
    data = json.loads(response.text)

    assert response.status_code == 201
    assert "_id" in data["data"]
    assert "title" in data["data"]
    assert "year" in data["data"]

    add_variable("user_movie_1", data["data"]["_id"])
