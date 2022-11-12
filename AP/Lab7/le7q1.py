#1. Create a function that writes the Fibonacci series up to n numbers.
def fibb(n):
    a=0
    b=1
    on=0
    if n==1:
        print(a,end=" ")
    elif n>=2:
        print(a,b,end=" ")
    n=n-2
    while(n>0):
        on=a+b
        print(on,end=" ")
        a=b
        b=on
        if(n!=0):
            n-=1
n = int(input("Enter the Number = "))
fibb(n)
