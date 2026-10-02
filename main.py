import json

def load_inventory():
    try:
        with open('inventory.json', 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def add_product():
    with open('inventory.json', 'r') as file:
        data = json.load(file)

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

    with open('inventory.json', 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Product '{product_name}' added to inventory.")
    print(data)
    
add_product()
