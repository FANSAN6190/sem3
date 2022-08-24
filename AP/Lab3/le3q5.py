#5. Calculate the factorial of the given number
def fac(n):
    f=1
    while n>0:
        f=n*f
        n-=1
    return f
n=int(input())
print("Factorial = ",fac(n))
