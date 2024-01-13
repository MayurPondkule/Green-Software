from flask import Flask, request, jsonify

app = Flask(__name__)

# temporary Product data
products = [
    {
        'id': 1,
        'name': 'laptop',
        'price': 45.80,
        'description': 'LENOVO laptop with 8GB RAM and 1 TB HDD'
    }
]

# temp cart data
carts = {}

# home
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Home Page"

# routes for handling different API endpoints

# Product Endpoints

@app.route('/display_products', methods=['GET'])
def get_all_products():
    return jsonify(products)

@app.route('/display_product/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({'message': 'Product not found'}), 404

@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON data'}), 400

    new_product = {
        'id': len(products) + 1,
        'name': data.get('name'),
        'price': data.get('price'),
        'description': data.get('description')
    }
    products.append(new_product)
    return jsonify(new_product), 201

# Cart Endpoints

@app.route('/cart/view', methods=['GET'])
def view_cart():
    # Get the user_id from the query parameter
    user_id = request.args.get('user_id')

    cart = carts.get(user_id, {})

    # Create a list to store cart items with additional details
    cart_items = []
    total_amount = 0

    # Iterate through the cart items
    for product_id, quantity in cart.items():
        # Try to find the product by its id in the products list
        product = next((p for p in products if p['id'] == product_id), None)
        if product:
            item_total = product['price'] * quantity
            total_amount += item_total
            cart_items.append({
                'product_id': product_id,
                'name': product['name'],
                'price': product['price'],
                'quantity': quantity,
                'item_total': item_total
            })

    # Prepare the response
    response_data = {
        'cart_items': cart_items,
        'total_amount': total_amount
    }

    # Return the response as JSON
    return jsonify(response_data)

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({'error': 'product not found '}), 404

    # add the product to the user's cart or update the quantity if the item is already in the cart
    cart = carts.get(user_id, {})
    cart[product_id] = cart.get(product_id, 0) + quantity
    carts[user_id] = cart

    return jsonify(cart)

@app.route('/cart/delete', methods=['POST'])
def delete_from_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')

    cart = carts.get(user_id, {})
    if product_id in cart:
        del cart[product_id]
        carts[user_id] = cart
        return jsonify({'message': 'Product removed from cart successfully'}), 200
    else:
        return jsonify({'error': 'Product not found in the cart'}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)
