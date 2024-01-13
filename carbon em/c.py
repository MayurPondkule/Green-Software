from codecarbon import OfflineEmissionsTracker



# Rest of your code

class Product:
    def __init__(self, id, name, price):
        self.name = name
        self.id = id
        self.price = price

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product):
        self.shopping_cart.add_product(products)

    def remove_from_cart(self, product):
        self.shopping_cart.remove_from_cart(products)

    def checkout(self):
        total = self.shopping_cart.cal_total()
        print(f"Total amount to pay: ${total}")

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(products)

    def remove_product(self, product):
        self.products.remove(products)

    def display_cart(self):
        if not self.products:
            print("Cart is empty")
        else:
            print("Cart contains the following Products")
            for product in self.products:
                print(f" - {products.name} (${products.price})")

    def remove_from_cart(self, product):
        if product in self.products:
            self.remove_product(products)
            print(f"Product {products.name} has been removed")
        else:
            print(f"{products.name} not in the cart")

    def cal_total(self):
        # tracker = OfflineEmissionsTracker(country_iso_code='IND')
        tracker = OfflineEmissionsTracker(country_iso_code='IND',track_mode="all", monitor_epochs=1, monitor_steps=1000)

        tracker.gpu = False
        
        tracker.start()
        
        total = 0
        for product in self.products:
            total = total+product.price
        tracker.stop()
        return total
       

# Interface

product1 = Product(1, "Dell 7490", 99999)
product2 = Product(2, "BMW", 5999999)
product3 = Product(3, "IPhone", 159999)
product4 = Product(4, "Shoes", 999)
product5 = Product(5, "Shirt", 599)

customer = Customer("Sarthak Redasani", "sarthak.22010800@viit.ac.in")
print("Welcome to Sarthak's E-commerce Store")
print("Products Available are:")

products = [product1, product2, product3, product4, product5]

for product in products:
    print(f"{product.id}, {product.name}, = ${product.price}")

while True:
    print("\nSelect an option from below")
    print("1: Add a product to the cart")
    print("2: Display Cart")
    print("3: Remove a product from the cart")
    print("4: Checkout")
    user_input = input("Enter your choice: ")

    if user_input == '1':
        print("Select a product to add to the cart")
        product_id = int(input("Enter product ID: "))
        selected_product = next((product for product in products if product.id == product_id), None)
        if selected_product:
            customer.add_to_cart(selected_product)
            print(f"Product {selected_product.name} added to the cart")
        else:
            print("Invalid Product")
    elif user_input == '2':
        customer.shopping_cart.display_cart()
    elif user_input == '3':
        print("Select a product to remove from the cart")
        product_id = int(input("Enter product ID: "))
        selected_product = next((product for product in products if product.id == product_id), None)
        if selected_product:
            customer.remove_from_cart(selected_product)
            print(f"Product {selected_product.name} removed from the cart")
        else:
            print("Invalid Product")
    elif user_input == '4':
        customer.checkout()
        break  # Exit the loop after checkout
    else:
        print("Invalid Input")