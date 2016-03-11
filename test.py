import unittest
from function import addition

class TestFunctionMethods(unittest.TestCase):

  def test_addition(self):
      self.assertEqual(addition(1,1), 2)
      self.assertEqual(addition(-1,1), 0)
      self.assertEqual(addition(4,4), 8)
      self.assertEqual(addition(-4,-4), -8)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctionMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)

