import requests
import json


def test_login_invalid_pass():
    url = "http://localhost:3000/api/users/tokens"

    payload = json.dumps({"email": "abc0000000.gro.com", "password": "nascar123"})
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, data=payload)
    data = json.loads(response.text)

    assert response.status_code == 400
    assert "error" in data
    assert "token" not in data
