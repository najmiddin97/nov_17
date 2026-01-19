def test_get_posts(api_client):
    response = api_client.get_posts()
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_post(api_client):
    data = {"title": "Test", "body": "This is a test", "userId": 1}
    response = api_client.create_post(data)
    assert response.status_code == 201
    assert response.json()['title'] == "Test"
