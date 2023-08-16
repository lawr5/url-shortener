def test_hello(client):
    response = client.get('/')
    assert b'Url Shortener' in response.data
