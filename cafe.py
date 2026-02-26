def admin_login():
    """ Function to handle admin login. It prompts the user for a username and password, then checks these credentials against entries in the 'admin.txt' file. If a match is found, it returns the username and role; otherwise, it indicates an invalid login attempt."""
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open("admin.txt", 'r') as f:
            for line in f:
                parts = line.strip().split(",")
                if parts[0] == username and parts[1] == password:
                    print("login successful")
                    return username, "admin"
        print("Invalid username or password.")

    except FileNotFoundError as e:
        print(e)
    return None, None


def staff_login():
    """ Function to handle staff login. Similar to the admin_login function, it prompts for credentials and checks them against the 'staff.txt' file. If a match is found, it returns the username and role; otherwise, it indicates an invalid login attempt."""
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open("staff.txt", 'r') as f:
            for line in f:
                parts = line.strip().split(",")
                if parts[0] == username and parts[1] == password:
                    print("login sucessfull")
                    return username, "staff"
        print("Invalid username or password.")

    except FileNotFoundError as e:
        print(e)
    return None, None


def view_products():
    """ Function to display the list of products. It reads from the 'products.txt' file and prints each product's name and price. If the file is not found, it handles the exception and informs the user."""
    try:
        with open("products.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                print(f"Name:{parts[0]} | price: {parts[1]}\n")
    except FileNotFoundError:
        print("Product File not found.")


def create_order():
    """ Function to create a new order. It prompts the user for order details and appends them to the 'orders.txt' file. If the file is not found, it handles the exception and informs the user."""
    try:
        order = input("Enter order Details : ")
        if order == "":
            print("Order cannot be empty.")
        else:
            with open("orders.txt", 'a') as f:
                f.write(order + '\n')
            print("Order created successfully.")

    except FileNotFoundError:
        print("Orders file not found.")


def create_product():
    """ Function to create a new product. It prompts the user for the product name and price, then appends this information to the 'products.txt' file. If the file is not found, it handles the exception and informs the user."""
    product_name = input("Enter Product name: ")
    price = input("Enter Product price: ")

    try:
        with open("products.txt", "a") as f:
            f.write(f"{product_name},{price}\n")
        print("Product created successfully.")

    except FileNotFoundError:
        print("Products file not found.")
        return


def main():
    """ Main function to run the cafe management system. It prompts the user to identify as either an admin or staff, then allows them to view products or create products/orders based on their role. The program continues to loop until the user decides to exit."""
    while True:
        choice = input("Are you an admin or staff? (admin/staff): ")
        if choice.lower() == "admin":
            user_role = admin_login()
            if user_role[0] is not None:
                d = input(
                    "Do you want to view products or create product? (view/create): ")
                if d.lower() == "view":
                    view_products()
                elif d.lower() == "create":
                    create_product()
            else:
                print("Invalid choice.")

        elif choice.lower() == "staff":
            if staff_login()[0] is not None:
                c = input(
                    "Do you want to view products or create order? (view/create): ")
                if c.lower() == "view":
                    view_products()
                elif c.lower() == "create":
                    create_order()
            else:
                print("Invalid choice.")
        else:
            print("Invalid choice.")

        # loops back to the start of the program
        choice2 = input("Do you want to continue? (yes/no): ")
        if choice2.lower() != "yes":
            print("Thank you")
            break


main()
