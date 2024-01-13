from a import app

def t():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b'<p>Welcome to the Home Page</p>' in response.data


