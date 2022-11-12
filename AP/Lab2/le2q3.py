#3: Write a python program for calculating simple and compound interest.
p=int(input("Enter the Principle amount = "))
r=int(input("Enter the rate of interest = "))
t=int(input("Enter the Time in years = "))
si=p*r*t/100
n=int(input("Enter the fryquency = "))
ci=(p*(1+r/n)**n*t)-p
print("Simple intrest = ",si)
print("Compund intrest = ",ci)


