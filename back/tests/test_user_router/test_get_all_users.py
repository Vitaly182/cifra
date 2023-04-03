

def test_200(test_client):
    response = test_client.get('/users/', params={
        'limit': 50,
        'offset': 0
    })
    assert response.status_code == 200
    json_data_keys = response.json().keys()
    for key in ['items', 'limit', 'offset', 'total']:
        assert key in json_data_keys

def test_422(test_client):
    response = test_client.get('/users/', params={
        'limit': 50,
    })
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'field required'

    response = test_client.get('/users/', params={
        'limit': 50.1,
        'offset': 0
    })
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'value is not a valid integer'

def test_params(test_client):
    response = test_client('/users/', params={
        'limit': 101,
        'offset': 0
    })
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'ensure this value is less than or equal to 100'