#3. Calculate compound interest.
def ci(p,r,t,n):
    return (p*(1+r/n)**n*t)-p
p=int(input("Enter the Principle amount = "))
r=int(input("Enter the rate of interest = "))
t=int(input("Enter the Time in years = "))
n=int(input("Enter the fryquency = "))
print("Compund intrest = ",ci(p,r,t,n))
