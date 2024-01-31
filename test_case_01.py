import requests


def test_healthy_check():
    url = "http://localhost:3000/"

    payload = {}
    headers = {"x-api-key": "MyUniqueApiKey"}

    response = requests.get(url, headers=headers, data=payload)

    assert response.text == '{"STATUS":"Good to go!"}'
    assert response.status_code == 200
