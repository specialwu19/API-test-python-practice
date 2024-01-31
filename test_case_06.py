import requests
import json
from share_variable import get_variable, add_variable


def test_login_valid_pass():
    url = "http://localhost:3000/api/users/tokens"

    payload = json.dumps({"email": get_variable("user_email"), "password": "nascar123"})
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, data=payload)
    data = json.loads(response.text)

    assert response.status_code == 200
    assert "token" in data["data"]

    add_variable("user_token", data["data"]["token"])
