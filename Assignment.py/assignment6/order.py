# shweta p
from file_handling import read_menu_from_file   # Import  read menu items from file
from exception import InvalidMenuItemError, InsufficientQuantityError   # Import Order exceptions

class Order:
    def __init__(self):
        self.items = [] # list to store items 

    def add_item(self, name, quantity):
        menu_items = read_menu_from_file()  
        for item in menu_items: 
            if item.name == name:  
                if item.quantity < quantity:   
                    raise InsufficientQuantityError("Insufficient quantity.")
                self.items.append((item, quantity)) # Add item and quantity to the order
                return
        raise InvalidMenuItemError("Menu item not found.")  # error if item not found

    def calculate_total(self):
        total = sum(item.price * quantity for item, quantity in self.items) # Calculate total
        return total # Return the total cost

    def generate_receipt(self):
        print("Receipt:")
        for item, quantity in self.items:   # Iterate over each ordered item
            print(f"{item.name} x {quantity}: ${item.price * quantity:.2f}")    # Print item name, quantity, and cost ,.2f means after decimal 2no.
        print(f"Total: ${self.calculate_total():.2f}")  # total cost
    def take_order():
        order = Order() # Create a new Order object
        while True:
            name = input("Enter menu item name (or 'done' to finish): ")    #  enter menu item name or 'done' to finish
            if name.lower() == 'done':  
                break
            quantity = int(input("Enter quantity: "))  
            try:
                order.add_item(name, quantity)  
            except Exception as e:  # Handle exceptions
                print(f"Error: {e}")    #  error message
        return order    # Return the completed order
