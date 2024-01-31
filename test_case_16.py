import requests
from share_variable import get_variable


def test_get_specific_movie_invalid_fail():
    url = "http://localhost:3000/api/movies/:id"
    replace_value = get_variable("user_movie_1")
    new_url = url.replace(":id", replace_value)

    payload = ""
    headers = {}

    response = requests.get(new_url, headers=headers, data=payload)

    assert response.status_code == 401
