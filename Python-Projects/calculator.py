
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2


def calculator():
    print("===== Python Calculator =====")

    while True:
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Choose an operation (1-5): ")

        if choice == "5":
            print("Thank you for using Python Calculator!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            else:
                result = divide(num1, num2)

            print("Result:", result)

        except ValueError as error:
            print("Input error:", error)


if __name__ == "__main__":
    calculator()
