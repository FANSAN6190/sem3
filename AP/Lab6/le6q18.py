#18. Write a python script to create a dictionary odd to store first 50 odd numbers, their log2.
import math
OddLog={}
for i in range(1,100,2):
    OddLog.update({i:math.log2(i)})
print(OddLog)
