#https://github.com/ThunderIconoclast24/lab11-KC-JC.git
#Partner 1: John-Claude Hutchinson
#Partner 2: Kyle Ziegler


import unittest
from calculator import *
#my email is kyleziegler@ufl.edu for further collaboration


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertTrue(add(0,1)==1)
        self.assertTrue(add(1,1)==2)
        self.assertTrue(add(2,-1)==1)


    def test_subtract(self): # 3 assertions
        self.assertTrue(sub(1,0) == 1)
        self.assertTrue(sub(2,1) == 1)
        self.assertTrue(sub(2,-1) == 3)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 0), 0)
        self.assertEqual(mul(2, -2), -4)
        self.assertEqual(mul(2, 0.5), 1)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,1),2)
        self.assertEqual(div(2,-2),-1)
        self.assertEqual(div(2,0.5),4)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self): # 3 assertions
        self.assertTrue(log(3,9)==0.5)
        self.assertTrue(log(1,2)==0)
        self.assertTrue(log(2,0.5)==-1)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(-2,-4)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)
        self.assertEqual(log(3,9),2)

    def test_hypotenuse(self): # 3 assertions
        with self.assertRaises(ValueError):
            hypotenuse(0, 5)
            hypotenuse(2,0)
        self.assertEqual(hypotenuse(3,4),5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(sqrt(0),0)
        self.assertEqual(sqrt(1),1)
        self.assertEqual(sqrt(4),2)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()