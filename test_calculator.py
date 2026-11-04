#Latthaphok Singcahda 6887051

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add1(self):
            self.assertEqual(self.calc.add(-6, -6), -12)

    def test_add2(self):
            self.assertEqual(self.calc.add(-5, 2), -3)



    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(-2, -3), 1)



    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(3, -7), -21)




    def test_divide1(self):
            self.assertEqual(self.calc.divide(5, -2), 2)

    def test_divide2(self):
            self.assertEqual(self.calc.divide(10, 2), 5)




    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(-5, -3), -2)

    def test_modulo2(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.modulo(-5, 0)
        

if __name__ == '__main__':
    # print(5%2)
    # print(5%-2)
    # print(5%-20)
    print("hello hell")
    unittest.main()
