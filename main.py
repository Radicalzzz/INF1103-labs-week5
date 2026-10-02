import json

def load_inventory():
    try:
        with open('inventory.json', 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_inventory(data):
    with open('inventory.json', 'w') as file:
        json.dump(data, file, indent=4)

def add_product():
    data = load_inventory()

    product_name = input("Enter the product name: ").capitalize()
    price = float(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))

    product = {
        #:03d, 0 = fill empty spaces with zeros, 3 = use 3 digits, d = integer, 
        'id': f'P{len(data) + 1:03d}',
        'name': product_name,
        'price': price,
        'stock': quantity
    }
    data.append(product)
    save_inventory(data)
    print("Product added successfully!")
    
def display_all():
    data = load_inventory()
    print("\nCurrent Inventory:")
    print("-----------------------------------------------------------------")

    for product in data:
       print(
            f"ID: {product['id']} |",
            f"Name: {product['name']} |",
            f"Price: ${product['price']:.2f} |", # .2f = 2 decimal places | floating point value
            f"Stock: {product['stock']}"
        )
    print("-----------------------------------------------------------------")

def search_product():
    data = load_inventory()
    search_name = input("Enter the product ID to search: ").capitalize()

    found_products = [product for product in data if product['id'] == search_name]

    if found_products:
        print("\nSearch Results:")
        print("-----------------------------------------------------------------")
        for product in found_products:
            print(
                f"ID: {product['id']} |",
                f"Name: {product['name']} |",
                f"Price: ${product['price']:.2f} |",
                f"Stock: {product['stock']}"
            )
        print("-----------------------------------------------------------------")
    else:
        print("Product not found.")

search_product()