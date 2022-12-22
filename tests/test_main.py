import requests

api_url = 'http://localhost:8000'

def test_healthcheck():
    response = requests.get(f'{api_url}/__health')
    assert response.status_code == 200
def test_emptyTablecheck():
    response = requests.get(f'{api_url}/status')
    assert response.status_code == 200
    assert len((response.json())) == 1
def test_create():
    description = "test_create description"
    body_text = "test_create body"
    code = 1
    body = {"description": description, "body": body_text, "code": code}
    response = requests.post(f'{api_url}/status', json=body)
    assert response.status_code == 200
    assert response.json().get('description') == description
    assert response.json().get('body') == body_text
    assert response.json().get('code') == code

