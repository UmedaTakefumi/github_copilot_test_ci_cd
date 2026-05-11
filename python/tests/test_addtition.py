import sys, os, io
import uuid
import unittest


class TestCalc(unittest.TestCase):
  """ Calcクラスのテストケース """
  def hoge(self):
    self.counter = ""

  def setUp(self):
    """ テストメソッド実行前に呼び出されるメソッド """
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

    ## see also: https://qiita.com/dokeita/items/521510ddd0e0e2317d7b
    self.original_stdout = sys.stdout
    sys.stdout = io.StringIO()

    from Calc.calc import Calc
    self.calc    = Calc()
    self.counter = int(1);
    self.uuidgen = uuid.uuid4()

  def tearDown(self):
    """ テストメソッド実行後に呼び出されるメソッド """
    output = sys.stdout.getvalue()
    sys.stdout = self.original_stdout
    print(output)

  def test_add_positive_num_SerialNum_4c081197(self):
    """ 加法のテスト """
    # print(f"加法テスト: {self.uuidgen}")
    result = self.calc.simple_addition(0,1)
    self.assertEqual(result, 1)

  def test_add_positive_num_SerialNum_829f1d73(self):
    """ 0-1 加法のテスト """
    # print(f"加法テスト: {self.uuidgen}")
    result = self.calc.simple_addition(1,2)
    self.assertEqual(result, 3)

  def test_add_positive_num_0_2(self):
    """ 0-2 加法のテスト """
    # print(f"加法テスト: {self.uuidgen}")
    result = self.calc.simple_addition(2,3)
    self.assertEqual(result, 5)

  def test_add_positive_num_0_3(self):
    """ 0-3 加法のテスト """
    # print(f"加法テスト: {self.uuidgen}")
    result = self.calc.simple_addition(3,4)
    self.assertEqual(result, 7)

if __name__ == "__main__":

  unittest.main()

