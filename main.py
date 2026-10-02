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
    print(data)
    print("\nCurrent Inventory:")
    print("-----------------------------------------------------------------")

    for product in data:
       print(
            f"ID: {product['id']} |",
            f"Name: {product['name']} |",
            f"Price: ${product['price']:.02f} |",
            f"Stock: {product['stock']}"
        )
    print("-----------------------------------------------------------------")

display_all()
