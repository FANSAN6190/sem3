#19. Write a python to store prime numbers between 50 and100 along with their digit-sum.
import math
OddLog={}
for i in range(50,100):
    for j in range(2,i):
        p=0
        if i%j==0:
            p=-1
            break
    if(p!=-1):
        print(i)


