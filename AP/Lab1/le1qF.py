#F.Calculate compound interest.
p=float(input("Enter the Principal amount = "))
r=float(input("Enter the rate of intrest = "))
n=int(input("Enter the number of intrest compounded(anually) = "))
t=int(input("Enter the time in years = "))
CI=(p*(1+(r/n))**(n/t))-p
print("Componud intrest on given principal amount = ",CI)

