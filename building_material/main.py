from admin import view_stock, update_stock, assign_transporter
from user import place_order
from transporter import confirm_delivery
def menu():
    while True:
        print("\n Building Material Management System")
        print("1. Admin Login")
        print("2. User Portal")
        print("3. Transporter Portal")
        print("4. Exit")

        ch = input("Enter your choice: ")
        if ch == "1":
            print("\n-- Admin Panel --")
            print("1. View Stock")
            print("2. Update Stock")
            print("3. Assign Transporter")
            admin_choice = input("Select: ")
            if admin_choice == "1":
                view_stock()
            elif admin_choice == "2":
                update_stock()
            elif admin_choice == "3":
                assign_transporter()

        elif ch == "2":
            print("\n-- User Portal --")
            place_order()

        elif ch == "3":
            print("\n-- Transporter Panel --")
            confirm_delivery()

        elif ch == "4":
            print("Exiting...")
            break
        else:
            print("Invalid input.")

menu()
