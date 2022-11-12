#16. Write a program that asks the user to input 10 integers, and then prints the largest odd number
#    that was entered. If no odd number was entered, it should print a message to that effect.
t=10
m=0
while t:
    n=int(input("-- "))
    if n%2!=0 and n>m:
        m=n
    t-=1
print("Largest odd number is = ",m)

