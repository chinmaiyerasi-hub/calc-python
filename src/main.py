# -----------------------------------------
#     SIMPLE BUT BIG PYTHON CALCULATOR
# -----------------------------------------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def calculator():
    print("===================================")
    print("        PYTHON CALCULATOR")
    print("===================================")

    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power (a^b)")
        print("6. Modulus")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == '7':
            print("\nExiting calculator... Goodbye!")
            break

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid Input! Try again.")
            continue

        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number! Please enter numeric values.")
            continue

        print("\nResult:")

        if choice == '1':
            print(add(num1, num2))
        elif choice == '2':
            print(subtract(num1, num2))
        elif choice == '3':
            print(multiply(num1, num2))
        elif choice == '4':
            print(divide(num1, num2))
        elif choice == '5':
            print(power(num1, num2))
        elif choice == '6':
            print(modulus(num1, num2))

        print("\n-----------------------------------")

# Run program only when this file is executed directly
if __name__ == "__main__":
    calculator()

