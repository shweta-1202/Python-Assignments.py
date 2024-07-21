# shweta p

from menu import Menu   # Import  Menu for managing menu items
from order import Order     # Import Order  for handling customer orders
from file_handling import read_orders_from_file, write_orders_to_file   

def main():
    menu = Menu()   

    while True:
        print("\nRestaurant Management System")
        print("1. Manage Menu")
        print("2. Place Order")
        print("3. View Orders")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            manage_menu(menu)   
        elif choice == '2':
            place_order(menu)  
        elif choice == '3':
            view_orders()   
        elif choice == '4':
            break  
        else:
            print("Invalid choice. Please try again.")

def manage_menu(menu):
    while True:
        print("\nMenu Management")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Delete Item")
        print("4. Display Menu")
        print("5. Back")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            try:
                menu.add_item(name, price, quantity)    #  add a new item to the menu
            except Exception as e:
                print(f"Error: {e}")     # error message 
        elif choice == '2':
            name = input("Enter item name: ")
            price = float(input("Enter new price: "))
            quantity = int(input("Enter new quantity: "))
            try:
                menu.update_item(name, price, quantity)  
            except Exception as e:
                print(f"Error: {e}")    # error message 
        elif choice == '3':
            name = input("Enter item name: ")
            try:
                menu.delete_item(name)  
            except Exception as e:
                print(f"Error: {e}")    
        elif choice == '4':
            menu.display_menu() # Display the current menu
        elif choice == '5':
            break   # Go back to the main menu
        else:
            print("Invalid choice. Please try again.")  # Prompt for valid input

def place_order(menu):
    order = Order()     # Create a new Order 
    order = Order.take_order()   #  to take an order
    order.generate_receipt()    # Generate and display the receipt for the order
    orders = read_orders_from_file()    # Read existing orders from file
    orders.append([(item.name, quantity) for item, quantity in order.items])    # Add the new order to the list
    write_orders_to_file(orders)    # Save the updated orders to file

def view_orders():
    orders = read_orders_from_file()
    for i, order in enumerate(orders, start=1):
        print(f"Order {i}:")
        for item, quantity in order:
            print(f"{item} x {quantity}")
        print()

main()
