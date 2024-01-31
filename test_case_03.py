import requests
import json
from utils import random_email
from share_variable import add_variable


def test_register_user_valid_pass():
    url = "http://localhost:3000/api/users/register"

    payload = json.dumps({"email": random_email(), "password": "nascar123"})

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, data=payload)
    data = json.loads(response.text)

    assert response.status_code == 201
    assert "_id" in data["data"]
    assert "email" in data["data"]

    add_variable("user_id", data["data"]["_id"])
    add_variable("user_email", data["data"]["email"])
