#21. Write a  program to find LCM of two numbers.
a=int(input("Enter the 1st number = "))
b=int(input("Enter the 2ed number = "))
for i in range(1,a):
    if a%i==0 and b%i==0:
        f=i
lcm=(a*b)/f
print(lcm)
