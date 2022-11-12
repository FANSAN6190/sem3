#10. Compute the volume of a cylinder, when its height and diameter is given.
def vc(h,d):
    print("Volume of cylinder = ",(3.14*h*(d/2)**2))
h=int(input("Entert the Height = "))
d=int(input("Enter the Diameter = "))
vc(h,d)

def vc(h,d):
    return (3.14*h*(d/2)**2)
h=int(input("Entert the Height = "))
d=int(input("Enter the Diameter = "))
print("Volume of cylinder = ",vc(h,d))
