import sys
import os
import unittest

class TestCalc(unittest.TestCase):
  """ Calcクラスのテストケース """
  def setUp(self):
    """ セットアップメソッド """
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

    from Calc.calc import Calc
    self.calc = Calc()

  def tearDown(self):
    """ クリーンアップメソッド """
    pass

  def test_add_positive_num(self):
    """ 加法のテスト """
    result = self.calc.simple_addition(2,3)
    self.assertEqual(result, 5)

if __name__ == "__main__":

  unittest.main()

