import requests


def test_healthy_check_fail():
    url = "http://localhost:3000/"

    payload = {}
    headers = {"x-api-key": "0000000000"}

    response = requests.get(url, headers=headers, data=payload)

    assert response.text == '{"error":{"code":999,"message":"Invalid API key"}}'
    assert response.status_code == 401
