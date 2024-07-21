import datetime

class Product:
    def __init__(self, name, category, price, quantity, expdate):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.expdate = expdate

    def __str__(self):
        return f"{self.name} ({self.category}): {self.quantity} available, ${self.price:.2f} each, Expires on {self.expdate}"

inventory = []  # Global list to store all products

def add_product(name, category, price, quantity, expdate):
    """Function to add a new product to the inventory."""
    product = Product(name, category, price, quantity, expdate)
    inventory.append(product)

def remove_product(product_name):
    """Function to remove a product from the inventory by name."""
    global inventory
    inventory = [product for product in inventory if product.name != product_name]

def search_products(search_term):
    """Function to search for products by name or category."""
    return [product for product in inventory if search_term.lower() in product.name.lower() or search_term.lower() in product.category.lower()]

def list_all_products():
    """Function to print details of all products in the inventory."""
    for product in inventory:
        print(product)

def categorize_products():
    """Function to categorize products by their category."""
    categories = {}
    for product in inventory:
        if product.category not in categories:
            categories[product.category] = []
        categories[product.category].append(product)
    return categories

def remove_expired_products():
    """Function to remove expired products from the inventory."""
    today = datetime.date.today()
    global inventory
    inventory = [product for product in inventory if product.expdate >= today]

def save_inventory(file_name):
    """Function to save the current inventory to a file."""
    try:
        with open(file_name, 'w') as file:
            for product in inventory:
                file.write(f"{product.name},{product.category},{product.price},{product.quantity},{product.expdate}\n")
        print("Inventory saved successfully.")
    except IOError:
        print(f"Error: Could not write to file {file_name}")

def load_inventory(file_name):
    """Function to load inventory data from a file."""
    try:
        with open(file_name, 'r') as file:
            for line in file:
                name, category, price, quantity, expdate = line.strip().split(',')
                product = Product(name, category, float(price), int(quantity), datetime.datetime.strptime(expdate, '%Y-%m-%d').date())
                inventory.append(product)
        print("Inventory loaded successfully.")
    except IOError:
        print(f"Error: Could not read file {file_name}")

def main():
    """Main function to run the Inventory Management System."""
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Search Products")
        print("4. List All Products")
        print("5. Categorize Products")
        print("6. Remove Expired Products")
        print("7. Save Inventory to File")
        print("8. Load Inventory from File")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            expdate = datetime.datetime.strptime(input("Enter product expiration date (YYYY-MM-DD): "), '%Y-%m-%d').date()
            add_product(name, category, price, quantity, expdate)
            print("Product added successfully.")

        elif choice == '2':
            product_name = input("Enter product name to remove: ")
            remove_product(product_name)
            print("Product removed successfully.")

        elif choice == '3':
            search_term = input("Enter product name or category to search: ")
            results = search_products(search_term)
            if results:
                for product in results:
                    print(product)
            else:
                print("No products found.")

        elif choice == '4':
            list_all_products()

        elif choice == '5':
            categorized = categorize_products()
            for category, products in categorized.items():
                print(f"Category: {category}")
                for product in products:
                    print(f"  - {product}")

        elif choice == '6':
            remove_expired_products()
            print("Expired products removed successfully.")

        elif choice == '7':
            file_name = input("Enter file name to save inventory: ")
            save_inventory(file_name)

        elif choice == '8':
            file_name = input("Enter file name to load inventory: ")
            load_inventory(file_name)

        elif choice == '9':
            print("Thank you for visiting the Inventory Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
