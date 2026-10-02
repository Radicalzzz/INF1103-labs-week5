import json

def load_inventory():
    global data
    with open('inventory.json', 'r') as file:
        data = json.load(file)
        print(data)

def add_product():
    with open('inventory.json', 'r') as file:
        data = json.load(file)

    product_name = input("Enter the product name: ")
    price = float(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))

    product = {
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
