import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
import newmath

class NewmathTestCase(unittest.TestCase):
  def test_divide_by_number(self):
    self.assertEqual(2, newmath.div(6, 3))

  def test_divide_by_zero(self):
    with self.assertRaises(ZeroDivisionError):
      newmath.div(10, 0)

if __name__ == '__main__':
    unittest.main()