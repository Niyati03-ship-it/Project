import json

from user import save_data

def load_data():
    with open("database.json", "r") as f:
        return json.load(f)

def confirm_delivery():
    transporter = input("Enter your name (transporter): ")
    data = load_data()
    deliveries = data["deliveries"]

    for delivery in deliveries:
        if delivery["transporter"] == transporter and not delivery.get("delivered", False):
            print(f"\n Delivery for {delivery['user']}")
            input("Press Enter after delivery...")
            delivery["delivered"] = True
            print("Delivery confirmed.")

    save_data(data)
