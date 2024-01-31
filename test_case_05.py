import requests
import json
import pytest


@pytest.fixture(scope="module")
def register_user_invalid():
    url = "http://localhost:3000/api/users/register"

    payload = json.dumps({"email": "abc12876.gro.com", "password": "nascar123"})
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, data=payload)
    return response


def test_get_expect_status_code_fail(register_user_invalid):
    assert register_user_invalid.status_code == 400


def test_get_data_invalid_pass(register_user_invalid):
    data = json.loads(register_user_invalid.text)
    assert "_id" not in data
    assert "email" not in data
