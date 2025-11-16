import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): # 3 assertions
        self.assertEqual(add(4, 9), 13)
        self.assertEqual(add(36,64),100)
        self.assertEqual(add(0,49),49)
    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(23,12),11)
        self.assertEqual(sub(13, 9),4)
        self.assertEqual(sub(654, 321), 333)
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,25)
    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2,4), 2)
        self.assertEqual(log(5,625),4)
        self.assertEqual(log(3,729),6)
    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(3, 0)

if __name__ == "__main__":
    unittest.main()