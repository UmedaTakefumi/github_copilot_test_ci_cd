import sys
#print("---------------------------")
#for temp in sys.path:
#  print(temp)
#print("---------------------------")

from Calc.calc import Calc

hoge = Calc()
result = hoge.simple_addition(2,3)
print(result)

