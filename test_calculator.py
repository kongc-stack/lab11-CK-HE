# https://github.com/kongc-stack/lab11-CK-HE.git
# Partner 1: Catherine Kong
# Partner 2: Hannah Elotmani

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

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertAlmostEqual(mul(4, 5), 20)
        self.assertAlmostEqual(mul(-4, -5),20)
        self.assertAlmostEqual(mul(4, 0), 0)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(4,20),5)
        with self.assertAlmostEqual(ZeroDivisionError):
            div(0, 20)
        self.assertAlmostEqual(div(-4, 20),-5)
    # ##########################



    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

        with self.assertRaises(ValueError):
            logarithm(-1, 1) #




    def test_hypotenuse(self): # 3 assertions
    #     fill in code
        self.assertAlmostEqual(hypotenuse(3,4))
        self.assertAlmostEqual(hypotenuse(-3, 4))
        self.assertAlmostEqual(hypotenuse(3,-4))

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
        with self.assertRaises(ValueError):
            square_root(-1)

        self.assertAlmostEqual(square_root(3))
        self.assertAlmostEqual(square_root(0))

    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()