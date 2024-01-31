import requests
from share_variable import get_variable
import json


def test_delete_specific_movie_valid_pass():
    url = "http://localhost:3000/api/movies/0000000000"

    payload = ""
    headers = {"Authorization": f'Bearer {get_variable("user_token")}'}

    response = requests.delete(url, headers=headers, data=payload)
    data = json.loads(response.text)

    assert response.status_code == 400
    assert "error" in data
