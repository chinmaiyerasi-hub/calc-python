import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """Unit tests for the Calculator class."""

    def setUp(self):
        """Create a Calculator instance before each test."""
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-2, 2), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(6, 7), 42)
        self.assertEqual(self.calc.multiply(-1, 5), -5)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(5, 0), "Error! Cannot divide by zero.")

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)

    def test_modulus(self):
        self.assertEqual(self.calc.modulus(10, 3), 1)
        self.assertEqual(self.calc.modulus(7, 7), 0)


if __name__ == "__main__":
    unittest.main()
