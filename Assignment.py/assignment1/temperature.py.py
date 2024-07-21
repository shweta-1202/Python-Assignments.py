def cel_to_fah(celsius):
    return (celsius * 9 / 5) + 32


def fah_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    while True:
        print("\nTemperature Conversion Tool")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            celsius = input("Enter the temperature in Celsius: ")
            try:
                celsius = float(celsius)
                fahrenheit = cel_to_fah(celsius)
                print(f"{celsius:.2f} Celsius is {fahrenheit:.2f} Fahrenheit.")
            except ValueError:
                print("Invalid temperature input. Please enter a valid number.")

        elif choice == '2':
            fahrenheit = input("Enter the temperature in Fahrenheit: ")
            try:
                fahrenheit = float(fahrenheit)
                celsius = fah_to_cel(fahrenheit)
                print(f"{fahrenheit:.2f} Fahrenheit is {celsius:.2f} Celsius.")
            except ValueError:
                print("Invalid temperature input. Please enter a valid number.")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
