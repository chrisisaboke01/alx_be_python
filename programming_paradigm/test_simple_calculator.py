import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-3, -2), -1)
        self.assertEqual(self.calc.subtract(10, 0), 10)

    def test_multiply(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-3, -2), 6)

    def test_divide(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertIsNone(self.calc.divide(10, 0))  # Test division by zero

    def test_edge_cases(self):
        """Test additional edge cases."""
        self.assertEqual(self.calc.add(1e10, 1e10), 2e10)  # Large numbers
        self.assertEqual(self.calc.subtract(1e10, 1e10), 0)
        self.assertEqual(self.calc.multiply(1e10, 0), 0)
        self.assertEqual(self.calc.divide(1e-10, 1e10), 1e-20)  # Very small numbers

if __name__ == "__main__":
    unittest.main()
