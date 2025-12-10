import unittest

from class_calculator import *

class TestClassCalculator(unittest.TestCase):
    
    def test_add(self):
        sum = Calculator(1,2)
        self.assertEqual(3,sum.add())

    def test_subtract(self):
        difference = Calculator(5,2)
        self.assertEqual(3,difference.subtract())
        

    def test_multiply(self):
        product = Calculator(1,2)
        self.assertEqual(2,product.multiply())

    def test_divide(self):
        quotient = Calculator(1,2)
        self.assertEqual(0.5,quotient.divide())




if __name__ == "__main__":
    unittest.main()