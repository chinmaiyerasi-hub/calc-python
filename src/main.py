"""
calculator.py

A simple, maintainable calculator implemented as a class.
Supports add, subtract, multiply, divide, power, and modulus.
"""

class Calculator:
    """A simple calculator class."""

    def add(self, a: float, b: float) -> float:
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Return the product of a and b."""
        return a * b

    def divide(self, a: float, b: float) -> float | str:
        """Return the division of a by b. Returns error if b is zero."""
        if b == 0:
            return "Error! Cannot divide by zero."
        return a / b

    def power(self, a: float, b: float) -> float:
        """Return a raised to the power of b."""
        return a ** b

    def modulus(self, a: float, b: float) -> float:
        """Return the remainder of a divided by b."""
        return a % b


def main():
    """Main function to run the calculator CLI."""
    calc = Calculator()
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

        operations = {
            '1': calc.add,
            '2': calc.subtract,
            '3': calc.multiply,
            '4': calc.divide,
            '5': calc.power,
            '6': calc.modulus
        }

        result = operations[choice](num1, num2)
        print(result)
        print("\n-----------------------------------")


if __name__ == "__main__":
    main()
