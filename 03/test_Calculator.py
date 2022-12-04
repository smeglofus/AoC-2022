from unittest import TestCase
from Calculator import Calculator


class TestCalculator(TestCase):
    calc = Calculator()

    def test_nasob(self):
        self.assertEqual(6,self.calc.nasob(2,3))

    def test_vydel(self):
        self.assertEqual(2,self.calc.vydel(4,2))

    def test_scitej(self):
        self.assertEqual(10,self.calc.scitej(5,5))

    def test_odecitej(self):
        self.assertEqual(5,self.calc.odecitej(10,5))
