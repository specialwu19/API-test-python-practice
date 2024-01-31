import requests
import json
from share_variable import get_variable
from utils import is_array

def test_get_movie_list_valid_pass():
    
    url = "http://localhost:3000/api/movies"

    payload = ""
    headers = {
    'Authorization': f'Bearer {get_variable("user_token")}'
    }

    response = requests.get(url, headers=headers, data=payload)
    data=json.loads(response.text)
     
    assert response.status_code==200
    assert is_array(data["data"])
    
    for item in data.get("data",[]):
        assert "_id" in item
        assert "owner" in item
        assert "title" in item
        assert "year" in item
        
