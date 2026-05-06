import sys
import os
import unittest


class TestCalc(unittest.TestCase):
  """ Calcクラスのテストケース """
  def setUp(self):
    """ セットアップメソッド """
    self.calc = Calc()

  def tearDown(self):
    """ クリーンアップメソッド """
    pass

  def test_add_positive_num(self):
    """ 加法のテスト """
    result = self.calc.simple_addition(2,3)
    self.assertEqual(result, 5)

if __name__ == "__main__":

print("---------------------------")
for temp in sys.path:
  print(temp)
print("---------------------------")
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
for temp in sys.path:
  print(temp)
print("---------------------------")

print(os.getcwd())
os.chdir('python')
print(os.getcwd())
print("---------------------------")

#from Calc.calc import Calc
#hoge = Calc()
#result = hoge.simple_addition(2,3)
#print(result)

unittest.main()

