import json

def load_data():
    with open("database.json", "r") as f:
        return json.load(f)

def save_data(data):
    with open("database.json", "w") as f:
        json.dump(data, f, indent=4)

def place_order():
    name = input("Enter your name: ")
    bricks = int(input("No. of bricks: "))
    cement = int(input("No. of cement sacks: "))
    sand = int(input("Amount of sand (kg): "))

    data = load_data()
    stock = data["stock"]
    
    if stock["bricks"] >= bricks and stock["cement"] >= cement and stock["sand"] >= sand:
        stock["bricks"] -= bricks
        stock["cement"] -= cement
        stock["sand"] -= sand

        order = {
            "user": name,
            "bricks": bricks,
            "cement": cement,
            "sand": sand,
            "assigned": False
        }
        data["orders"].append(order)
        save_data(data)
        print(" Order placed successfully!")
    else:
        print(" Insufficient stock for your order.")


