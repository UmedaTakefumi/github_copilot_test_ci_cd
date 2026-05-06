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

  def test_add_positive_num_0_1(self):
    """ 0-1 加法のテスト """
    result = self.calc.simple_addition(1,2)
    self.assertEqual(result, 3)

  def test_add_positive_num_0_2(self):
    """ 0-2 加法のテスト """
    result = self.calc.simple_addition(2,3)
    self.assertEqual(result, 5)

  def test_add_positive_num_0_3(self):
    """ 0-3 加法のテスト """
    result = self.calc.simple_addition(3,4)
    self.assertEqual(result, 7)

if __name__ == "__main__":

  unittest.main()

