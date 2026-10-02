import json

def load_inventory():
    with open('inventory.json', 'r') as file:
        data = json.load(file)
        # total_units = data.get('total_units', 0)
        # history = data.get('history', [])
        # return total_units, history
        print(data)

load_inventory()