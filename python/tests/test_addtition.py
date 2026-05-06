import sys
import os

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

from Calc.calc import Calc
hoge = Calc()
result = hoge.simple_addition(2,3)
print(result)





