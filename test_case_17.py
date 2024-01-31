import requests
from share_variable import get_variable
import json


def test_delete_specific_movie_valid_pass():
    url = "http://localhost:3000/api/movies/:id"
    replace_value = get_variable("user_movie_1")
    new_url = url.replace(":id", replace_value)

    payload = ""
    headers = {"Authorization": f'Bearer {get_variable("user_token")}'}

    response = requests.delete(new_url, headers=headers, data=payload)
    data = json.loads(response.text)

    assert response.status_code == 200
    assert "Delete Success" in data["data"]["message"]
    assert data["data"]["_id"] == get_variable("user_movie_1")
