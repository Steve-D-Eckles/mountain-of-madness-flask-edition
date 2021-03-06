import madness

def test_import():
    assert madness

def test_config():
    assert not madness.create_app().testing
    assert madness.create_app({'TESTING': True}).testing

def test_hello(client):
    response = client.get('/')
    assert b'The mountain awaits!' in response.data
