
class Product:
    def __init__(self,id, name, price):
        self.id = id
        self.name = name
        self.price = price


class ShoppingCart :
    def __init__(self):
        self.products=[]

    def add_product(self,product):
        self.products.append(product)

    def remove_product(self,product):
        self.products.remove(product)

    def display_cart(self):
        if not self.products:
            print("cart is empty")

        else:
            print("cart contains follwing items")
            for product in self.products:
                print(f"-{product.name}  (${product.price})")

    def remove_from_cart(self,product):
        if product in self.products:
            self.remove_product(product)
            print("Product{product.name} has been removed")
        else:print(f"{product.name} not found")

    def calculate_total(self):


        total=0;
        for product in self.products:
            total+=product.price;
        return total
        
        
        

    
class Customer:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.shopping_cart=ShoppingCart()

    def add_to_cart(self,product):
        self.shopping_cart.add_product(product)

    def remove_from_cart(self,product):
        self.shopping_cart.remove_from_cart(product)

    def checkout(self):
        total =self.shopping_cart.calculate_total()
        print(f"total amount to pay: {total}")

product1=Product (1,"iphone",1000)
product2=Product (2,"HeadPhone",3000)
product3=Product (3,"Lenovo",7000)
product4=Product (4,"Vivo",5000)
product5=Product (5,"dell laptop",8000)


Customer =Customer("Mayur Pondkule","mayur.22010670@viit.ac.in")
print("welcome to the ecommerce command line store")
print("Here are available products")

products=[product1,product2,product3,product4,product5]

for product in products:
    print(f"{product.id},{product.name}=${product.price}")


while True:
    print("\nSelect an option from below ")
    print("1:Add a product to the cart ")
    print("2:display Cart")
    print("3:remove a product from the cart ")
    print("4:checkout ")
          
    user_input=input("enter your choice:")

    if user_input =='1':
         print("Select a product  to add to the cart  ")
         product_id =int(input("enter product id "))
         selected_product=next ((product for product in products if product.id == product_id),None)
         if selected_product:
             Customer.add_to_cart(selected_product);
             print(f"Product {selected_product.name} added in the cart")
         else:
             print("invaliod id product ID specified ")
    
  
    elif user_input =='2':
        Customer.shopping_cart.display_cart()

    elif user_input =='3':
        # Customer.shopping_cart.remove_from_cart()
         print("Select a product  to remove to the cart  ")
         product_id =int(input("enter product id "))
         selected_product=next ((product for product in Customer.shopping_cart.products if product.id==product_id),None)
         if selected_product:
             Customer.remove_from_cart(selected_product);
             print(f"Product {selected_product.name} added in the cart")
         else:
             print("invaliod id product ID specified ")

    elif user_input =='4':
        Customer.checkout();
        break
    

    else:
         print("enter valid ")
    