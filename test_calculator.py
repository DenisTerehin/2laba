# test_calculator.py
import unittest
from calculator_operations import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.add(3, 5)
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = self.calculator.subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiplication(self):
        result = self.calculator.multiply(2, 6)
        self.assertEqual(result, 12)

if __name__ == "__main__":
    unittest.main()
