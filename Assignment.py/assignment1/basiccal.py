def calculator():
    print("Welcome to the basic calculator!")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")

    while True:
        choice = input("Enter choice (1, 2, 3, 4, 5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice! Please enter a valid choice.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = num1 + num2
                print(f"Result of addition is: {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"Result of subtraction is: {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"Result of multiplication is: {result}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
                print(f"Result of division is: {result}")

        except ValueError:
            print("Invalid input! Please enter numeric values.")


calculator()