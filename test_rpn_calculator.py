import unittest
from rpn_calculator import Calculator


class TestRpnCalculator(unittest.TestCase):
    def test_calc(self):
        calc = Calculator()
        self.assertEqual(0, calc.evaluate("0"))
        self.assertEqual(3, calc.evaluate("1+2"))
        self.assertEqual(3.5, calc.evaluate("1+2.5"))
        self.assertEqual(-3, calc.evaluate("0-3"))
        self.assertEqual(6, calc.evaluate("1+2.5*2"))
        self.assertEqual(-2.5, calc.evaluate("1-3.5/1"))
        self.assertEqual(3, calc.evaluate("(1+2)*(2-1)"))
        self.assertEqual(2, calc.evaluate("2*(4-(1+2))"))
        self.assertEqual(3, calc.evaluate("2*4-5"))
        self.assertEqual(8, calc.evaluate("2*2*2"))
        self.assertEqual(-1, calc.evaluate("3/-3"))
        self.assertEqual(-4, calc.evaluate("-2*2"))


if __name__ == '__main__':
    unittest.main()
