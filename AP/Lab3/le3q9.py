#9. Compute the area of a cylinder, when its height and diameter is given.
def sarc(h,d):
    print("Surface Area of cylinder = ",(2*3.14*(d/2)*((d/2)+h)))
h=int(input("Entert the Height = "))
d=int(input("Enter the Diameter = "))

def sarc(h,d):
    return 2*3.14*(d/2)*((d/2)+h)
h=int(input("Entert the Height = "))
d=int(input("Enter the Diameter = "))
print("Surface Area of cylinder = ",sarc(h,d))

