import unittest
from Chapter23 import doOr

class TestFunctionMethods(unittest.TestCase):

  def test_or(self):
    self.assertTrue(doOr(1,1))
    self.assertTrue(doOr(0,1))
    self.assertTrue(doOr(1,0))
    self.assertFalse(doOr(0,0))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunctionMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)

