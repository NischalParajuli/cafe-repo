# Registration and login functions for admin, staff, and customer

def register_admin():
    username = input("Enter username: ")
    password = input("Enter password: ")
    try:
        with open("admin.txt", 'a') as f:
            f.write(f"{username},{password}\n")
        print("Registration successful.")
    except FileNotFoundError as e:
        print(e)


def register_staff():
    username = input("Enter username: ")
    password = input("Enter password: ")
    try:
        with open("staff.txt", 'a') as f:
            f.write(f"{username},{password}\n")
        print("Registration successful.")
    except FileNotFoundError as e:
        print(e)


def register_customer():
    username = input("Enter username: ")
    password = input("Enter password: ")
    try:
        with open("customer.txt", 'a') as f:
            f.write(f"{username},{password}\n")
        print("Registration successful.")
    except FileNotFoundError as e:
        print(e)


def admin_login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    try:
        with open("admin.txt", 'r') as f:
            for line in f:
                parts = line.strip().split(",")
                if parts[0] == username and parts[1] == password:
                    print("Login successful.")
                    return username, "admin"
        print("Invalid username or password.")
    except FileNotFoundError as e:
        print(e)
    return None, None


def staff_login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    try:
        with open("staff.txt", 'r') as f:
            for line in f:
                parts = line.strip().split(",")
                if parts[0] == username and parts[1] == password:
                    print("Login successful.")
                    return username, "staff"
        print("Invalid username or password.")
    except FileNotFoundError as e:
        print(e)
    return None, None


def customer_login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    try:
        with open("customer.txt", 'r') as f:
            for line in f:
                parts = line.strip().split(",")
                if parts[0] == username and parts[1] == password:
                    print("Login successful.")
                    return username, "customer"
        print("Invalid username or password.")
    except FileNotFoundError as e:
        print(e)
    return None, None

# Product viewing and order creation functions

def view_products():
    try:
        with open("products.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                print(f"Name: {parts[0]} | Price: {parts[1]}\n")
    except FileNotFoundError:
        print("Product file not found.")


def create_order():
    try:
        order = input("Enter order details: ")
        if order == "":
            print("Order cannot be empty.")
        else:
            with open("orders.txt", 'a') as f:
                f.write(order + '\n')
            print("Order created successfully.")
    except FileNotFoundError:
        print("Orders file not found.")


def create_product():
    product_name = input("Enter product name: ")
    price = input("Enter product price: ")
    try:
        with open("products.txt", "a") as f:
            f.write(f"{product_name},{price}\n")
        print("Product created successfully.")
    except FileNotFoundError:
        print("Products file not found.")

# Main function to handle user interactions

def main():
    while True:
        choice = int(input("1) Register | 2) Login | 3) Exit: "))

        if choice == 1:
            register_choice = int(
                input("Register as: (1) Admin / (2) Staff / (3) Customer: "))
            if register_choice == 1:
                register_admin()
            elif register_choice == 2:
                register_staff()
            elif register_choice == 3:
                register_customer()
            else:
                print("Invalid choice.")

        elif choice == 2:
            login_choice = int(
                input("Login as: (1) Admin / (2) Staff / (3) Customer: "))

            if login_choice == 1:
                user_role = admin_login()
                if user_role[0] is not None:
                    d = input(
                        "View products or create product? (view/create): ")
                    if d.lower() == "view":
                        view_products()
                    elif d.lower() == "create":
                        create_product()
                    else:
                        print("Invalid choice.")

            elif login_choice == 2:                         
                user_role = staff_login()
                if user_role[0] is not None:
                    c = input("View products or create order? (view/create): ")
                    if c.lower() == "view":
                        view_products()
                    elif c.lower() == "create":
                        create_order()
                    else:
                        print("Invalid choice.")

            elif login_choice == 3:                        
                user_role = customer_login()
                if user_role[0] is not None:
                    view_products()

            else:
                print("Invalid choice.")

        elif choice == 3:
            print("Thank you!")
            break

        else:
            print("Invalid choice.")
            
# Ask user if they want to continue or exit

        choice2 = int(input("Do you want to continue? (1) Yes / (2) No: "))
        if choice2 != 1:
            print("Thank you!")
            break


main()
