import requests
from share_variable import get_variable
import json


def test_get_specific_movie_invalid_pass():
    url = "http://localhost:3000/api/movies/0000000000"

    payload = ""
    headers = {"Authorization": f'Bearer {get_variable("user_token")}'}

    response = requests.get(url, headers=headers, data=payload)
    data = json.loads(response.text)

    assert response.status_code == 400
    assert "error" in data
    assert "_id" not in data
    assert "title" not in data
    assert "year" not in data
    assert "owner" not in data
