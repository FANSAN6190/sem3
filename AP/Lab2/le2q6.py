#6: Write a python program to calculate sum of 6 subjects and find percentage obtained.
print("Enter marks out of 30")
a=int(input("s1="))
b=int(input("s2="))
c=int(input("s3="))
d=int(input("s4="))
e=int(input("s5="))
f=int(input("s6="))
sm=a+b+c+d+e+f
pc=sm*100/(6*30)
print("Sum = ",sm,"   Percentage = ",pc)
