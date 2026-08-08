import json

def load_data():
    with open("database.json", "r") as f:
        return json.load(f)

def save_data(data):
    with open("database.json", "w") as f:
        json.dump(data, f, indent=4)

def view_stock():
    data = load_data()
    print("Current Stock:")
    for item, qty in data["stock"].items():
        print(f"  {item.capitalize()}: {qty}")

def update_stock():
    data = load_data()
    item = input("Enter material (bricks/cement/sand): ").lower()
    if item in data["stock"]:
        qty = int(input(f"Enter quantity to add in {item}: "))
        data["stock"][item] += qty
        save_data(data)
        print(f" {qty} added to {item}.")
    else:
        print(" Invalid material.")

def assign_transporter():
    data = load_data()
    for i, order in enumerate(data["orders"]):
        if not order["assigned"]:
            print(f"\nOrder {i+1}: {order}")
            confirm = input("Assign transporter to this order? (y/n): ")
            if confirm.lower() == 'y':
                transporter = input("Enter transporter name: ")
                order["assigned"] = True
                order["transporter"] = transporter
                data["deliveries"].append(order)
                print(f" Assigned to {transporter}")
    save_data(data)
