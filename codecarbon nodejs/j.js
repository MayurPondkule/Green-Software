class Product {
    constructor(id, name, price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }
}

class ShoppingCart {
    constructor() {
        this.products = [];
    }

    addProduct(product) {
        this.products.push(product);
    }

    removeProduct(product) {
        const index = this.products.indexOf(product);
        if (index !== -1) {
            this.products.splice(index, 1);
        }
    }

    displayCart() {
        if (this.products.length === 0) {
            console.log("Cart is empty");
        } else {
            console.log("Cart contains the following items:");
            this.products.forEach(product => {
                console.log(`-${product.name}  ($${product.price})`);
            });
        }
    }

    removeFromCart(product) {
        const index = this.products.indexOf(product);
        if (index !== -1) {
            this.removeProduct(product);
            console.log(`Product ${product.name} has been removed`);
        } else {
            console.log(`${product.name} not found`);
        }
    }

    calculateTotal() {
        return this.products.reduce((total, product) => total + product.price, 0);
    }
}

class Customer {
    constructor(name, email) {
        this.name = name;
        this.email = email;
        this.shoppingCart = new ShoppingCart();
    }

    addToCart(product) {
        this.shoppingCart.addProduct(product);
    }

    removeFromCart(product) {
        this.shoppingCart.removeFromCart(product);
    }

    checkout() {
        const total = this.shoppingCart.calculateTotal();
        console.log(`Total amount to pay: $${total}`);
    }
}

const product1 = new Product(1, "iphone", 1000);
const product2 = new Product(2, "HeadPhone", 3000);
const product3 = new Product(3, "Lenovo", 7000);
const product4 = new Product(4, "Vivo", 5000);
const product5 = new Product(5, "dell laptop", 8000);

const customer = new Customer("Mayur Pondkule", "mayur.22010670@viit.ac.in");

console.log("Welcome to the ecommerce command line store");
console.log("Here are available products");

const products = [product1, product2, product3, product4, product5];

products.forEach(product => {
    console.log(`${product.id}, ${product.name} = $${product.price}`);
});

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function getUserInput(question) {
    return new Promise(resolve => {
        rl.question(question, answer => {
            resolve(answer);
        });
    });
}

(async function main() {
    while (true) {
        console.log("\nSelect an option from below ");
        console.log("1: Add a product to the cart ");
        console.log("2: Display Cart");
        console.log("3: Remove a product from the cart ");
        console.log("4: Checkout ");

        const user_input = await getUserInput("Enter your choice: ");

        if (user_input === '1') {
            console.log("Select a product to add to the cart ");
            const product_id = parseInt(await getUserInput("Enter product id: "));
            const selected_product = products.find(product => product.id === product_id);
            if (selected_product) {
                customer.addToCart(selected_product);
                console.log(`Product ${selected_product.name} added to the cart`);
            } else {
                console.log("Invalid product ID specified");
            }
        } else if (user_input === '2') {
            customer.shoppingCart.displayCart();
        } else if (user_input === '3') {
            console.log("Select a product to remove from the cart ");
            const product_id = parseInt(await getUserInput("Enter product id: "));
            const selected_product = customer.shoppingCart.products.find(product => product.id === product_id);
            if (selected_product) {
                customer.removeFromCart(selected_product);
                console.log(`Product ${selected_product.name} removed from the cart`);
            } else {
                console.log("Invalid product ID specified");
            }
        } else if (user_input === '4') {
            customer.checkout();
            rl.close();
            break;
        } else {
            console.log("Enter a valid option");
        }
    }
})();
