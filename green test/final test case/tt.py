import pytest
from a import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_all_products(client):
    response = client.get('/display_products')
    assert response.status_code == 200
    # Add assertions to validate the response content, for example:
    assert b'laptop' in response.data
    assert b'LENOVO laptop' in response.data

def test_get_product_by_id(client):
    response = client.get('/display_product/1')
    assert response.status_code == 200
    # Add assertions to validate the response content for a specific product ID

def test_add_product(client):
    new_product = {
        'name': 'New Product',
        'price': 99.99,
        'description': 'This is a new product'
    }
    response = client.post('/add_product', json=new_product)
    assert response.status_code == 201
    # Add assertions to validate the response content after adding a new product

def test_view_cart(client):
    response = client.get('/cart/view?user_id=1')
    assert response.status_code == 200
    # Add assertions to validate the response content for viewing the cart

def test_add_to_cart(client):
    data = {
        'user_id': 1,
        'product_id': 1,
        'quantity': 2
    }
    response = client.post('/cart/add', json=data)
    assert response.status_code == 200
    # Add assertions to validate the response content after adding to the cart

def test_delete_from_cart(client):
    data = {
        'user_id': 1,
        'product_id': 1
    }
    response = client.post('/cart/delete', json=data)
    assert response.status_code == 200
    # Add assertions to validate the response content after deleting from the cart