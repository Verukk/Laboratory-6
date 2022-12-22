import unittest

from Calculator import Calculator
class TestCalculator(unittest.TestCase):
  def setUp(self):
    self.calculator = Calculator()
  def test_add(self):
    self.assertEqual(self.calculator.add(3,3), 6)
    self.assertEqual(self.calculator.add(3, 10), 13)
  def test_subtract(self):
    self.assertEqual(self.calculator.subtract(10,5), 5)
    self.assertEqual(self.calculator.subtract(3, 2), 1)
  def test_multiply(self):
    self.assertEqual(self.calculator.multiply(2,2), 4)
    self.assertEqual(self.calculator.multiply(2, 6), 12)
  def test_divide(self):
    self.assertEqual(self.calculator.divide(150,25), 6)
    self.assertEqual(self.calculator.divide(100, 10), 10)
  def test_dividetest(self):
    self.assertEqual(self.calculator.divide(200, 10), 20)

if __name__ == "__main__":
  unittest.main()
