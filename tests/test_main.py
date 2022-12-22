import requests

api_url = 'http://localhost:8000'
formatter = '/?format=json'
def test_healthcheck():
    response = requests.get(f'{api_url}/__health')
    assert response.status_code == 200
def test_emptyTablecheck_status():
    response = requests.get(f'{api_url}/status{formatter}')
    assert response.status_code == 200
    assert len((response.json())) == 0
def test_emptyTablecheck_Job():
    response = requests.get(f'{api_url}/job{formatter}')
    assert response.status_code == 200
    assert len((response.json())) == 0

def test_create_status():
    description = "test_create description"
    body_text = "test_create body"
    code = 1
    body = {"description": description, "body": body_text, "code": code}
    response = requests.post(f'{api_url}/status{formatter}', json=body)
    assert response.status_code == 201 # 201 - Created
    assert response.json().get('description') == description
    assert response.json().get('body') == body_text
    assert response.json().get('code') == code

def test_create_job():
    durability = 10
    category = "None"
    subJobs = 10
    body = {"durability" : durability, "category": category, "subJobs": subJobs}
    response = requests.post(f'{api_url}/job{formatter}', json=body)
    assert response.status_code == 201 # 201 - Created
    assert response.json().get("durability") == durability
    assert response.json().get("category") == category
    assert response.json().get("subJobs") == subJobs

def test_metrics():
    response = requests.get(f'{api_url}/metriscs')
    assert response.status_code == 200
    assert len((response.json())) != 0