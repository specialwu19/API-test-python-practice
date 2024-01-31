import requests
import json
from share_variable import get_variable


def test_register_user_invalid_pass():
    url = "http://localhost:3000/api/users/register"

    payload = json.dumps({"email": get_variable("user_email"), "password": "nascar123"})
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, data=payload)
    data = json.loads(response.text)

    assert response.status_code == 400
    assert "error" in data
    assert "_id" not in data
    assert "email" not in data
