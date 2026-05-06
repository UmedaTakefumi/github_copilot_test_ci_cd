import sys
#print("---------------------------")
#for temp in sys.path:
#  print(temp)
#print("---------------------------")

from Calc.calc import Calc

calc01 = Calc()
result01 = calc01.simple_addition(1,2)
print(result01)

calc02 = Calc()
result02 = calc02.simple_addition(2,3)
print(result02)

calc03 = Calc()
result03 = calc03.simple_addition(3,4)
print(result03)
