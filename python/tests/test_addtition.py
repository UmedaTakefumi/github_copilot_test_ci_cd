import sys, os, io
import uuid
import inspect
import unittest

class TestCalc(unittest.TestCase):
  """ Calcクラスのテストケース """

  def setUp(self):
    """ テストメソッド実行前に呼び出されるメソッド """
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

    ## see also: https://qiita.com/dokeita/items/521510ddd0e0e2317d7b
    self.original_stdout = sys.stdout
    sys.stdout = io.StringIO()

    from Calc.calc import Calc
    self.calc     = Calc()
    self.uuidgen  = uuid.uuid4()

  def tearDown(self):
    """ テストメソッド実行後に呼び出されるメソッド """

    ## see also: https://qiita.com/dokeita/items/521510ddd0e0e2317d7b
    output = sys.stdout.getvalue()
    sys.stdout = self.original_stdout
    print(output)

  def test_add_positive_num_SerialNum_4c081197(self):
    """ 加法テスト """

    ## see also: https://qiita.com/megmogmog1965/items/0b4ea3d58e34f1854158
    self.funcname = inspect.currentframe().f_code.co_name

    ## デバック用のPrint用途で利用する
    print(f"Debug-Print: {self.uuidgen}, {self.funcname}")

    result = self.calc.simple_addition(0,1)
    self.assertEqual(result, 1)

  def test_add_positive_num_SerialNum_829f1d73(self):
    """ 加法テスト """
    #""" 0-1 加法のテスト """ <= 連番つけると不便, 連番だめ, メソッド名にUUIDを付与する
    # print(f"加法テスト: {self.uuidgen}")
    result = self.calc.simple_addition(1,2)
    self.assertEqual(result, 3)

  def test_add_positive_num_SerialNum_bed917bc(self):
    """ 加法テスト """
    # print(f"加法テスト: {self.uuidgen}")
    result = self.calc.simple_addition(2,3)
    self.assertEqual(result, 5)

  def test_add_positive_num_SerialNum_f87d19e4(self):
    """ 加法テスト """
    # print(f"加法テスト: {self.uuidgen}")
    result = self.calc.simple_addition(3,4)
    self.assertEqual(result, 7)


if __name__ == "__main__":

  unittest.main()

