import requests
import pytest
from share_variable import get_variable


@pytest.fixture(scope="module")
def create_new_movie_invalid():
    url = "http://localhost:3000/api/movies"

    payload = '{\r\n  "title": "may",\r\n  "year": 1982\r\n}'
    headers = {
        "Authorization": f'Bearer {get_variable("user_token")}',
        "Content-Type": "text/plain",
    }

    response = requests.post(url, headers=headers, data=payload)

    return response


def test_get_expect_status_code_fail(create_new_movie_invalid):
    assert create_new_movie_invalid.status_code == 400


def test_get_data_invalid_fail(create_new_movie_invalid):
    data = create_new_movie_invalid.text
    assert "_id" not in data
    assert "title" not in data
    assert "year" not in data
