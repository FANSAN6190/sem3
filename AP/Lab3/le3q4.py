#4. Find the value of force when mass of a body and its acceleration is given.
def force(m,a=10):
    return m*a
m=int(input("Enter the mass = "))
a=int(input("Enter the acceleration="))
print("Force = ",force(m,a))
