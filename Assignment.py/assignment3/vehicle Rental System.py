class Vehicle:
    def __init__(self, vehicle_id, make, model, year, category):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.category = category

    def display_info(self):
        return f"ID: {self.vehicle_id}, Make: {self.make}, Model: {self.model}, Year: {self.year}, Category: {self.category}"

class VehicleManager:
    def __init__(self):
        self.vehicles = {}
    
    def add_vehicle(self, vehicle):
        if vehicle.vehicle_id in self.vehicles:
            print(f"Vehicle with ID {vehicle.vehicle_id} already exists.")
            return
        self.vehicles[vehicle.vehicle_id] = vehicle
        print(f"Vehicle {vehicle.display_info()} added successfully.")
    
    def remove_vehicle(self, vehicle_id):
        if vehicle_id not in self.vehicles:
            print(f"Vehicle with ID {vehicle_id} not found.")
            return
        del self.vehicles[vehicle_id]
        print(f"Vehicle with ID {vehicle_id} removed successfully.")
    
    def search_vehicle(self, term):
        term = term.lower()
        results = [v for v in self.vehicles.values() if term in v.make.lower() or term in v.model.lower()]
        if results:
            print("Vehicles found:")
            for vehicle in results:
                print(vehicle.display_info())
        else:
            print("No vehicles found.")
    
    def list_vehicles(self):
        if not self.vehicles:
            print("No vehicles available.")
            return
        for vehicle in self.vehicles.values():
            print(vehicle.display_info())
    
    def categorize_vehicles(self):
        categories = {}
        for vehicle in self.vehicles.values():
            if vehicle.category not in categories:
                categories[vehicle.category] = []
            categories[vehicle.category].append(vehicle.display_info())
        
        for category, vehicles in categories.items():
            print(f"\nCategory: {category}")
            for vehicle in vehicles:
                print(vehicle)
    
    def check_duplicates(self):
        vehicle_ids = list(self.vehicles.keys())
        if len(vehicle_ids) != len(set(vehicle_ids)):
            print("Duplicates detected.")
        else:
            print("No duplicates found.")

class VehicleRentalApp:
    def __init__(self):
        self.manager = VehicleManager()
    
    def display_menu(self):
        while True:
            print("\nVehicle Rental System Menu:")
            print("1. Add a Vehicle")
            print("2. Remove a Vehicle")
            print("3. Search for a Vehicle")
            print("4. List All Vehicles")
            print("5. Categorize Vehicles")
            print("6. Check for Duplicates")
            print("7. Exit")
            
            choice = input("Enter your choice (1-7): ").strip()
            if choice == '1':
                self.add_vehicle_ui()
            elif choice == '2':
                self.remove_vehicle_ui()
            elif choice == '3':
                self.search_vehicle_ui()
            elif choice == '4':
                self.manager.list_vehicles()
            elif choice == '5':
                self.manager.categorize_vehicles()
            elif choice == '6':
                self.manager.check_duplicates()
            elif choice == '7':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
    
    def add_vehicle_ui(self):
        try:
            vehicle_id = int(input("Enter Vehicle ID: "))
            make = input("Enter Make: ").strip()
            model = input("Enter Model: ").strip()
            year = int(input("Enter Year: "))
            category = input("Enter Category: ").strip()
            vehicle = Vehicle(vehicle_id, make, model, year, category)
            self.manager.add_vehicle(vehicle)
        except ValueError:
            print("Invalid input. Please ensure vehicle ID and year are integers.")
    
    def remove_vehicle_ui(self):
        try:
            vehicle_id = int(input("Enter the Vehicle ID to remove: "))
            self.manager.remove_vehicle(vehicle_id)
        except ValueError:
            print("Invalid input. Vehicle ID should be an integer.")
    
    def search_vehicle_ui(self):
        search_term = input("Enter the make or model to search for: ").strip()
        self.manager.search_vehicle(search_term)

app = VehicleRentalApp()
app.display_menu()





