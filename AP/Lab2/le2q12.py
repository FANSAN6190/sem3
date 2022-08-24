# 12: The length & breadth of a rectangle and radius of a circle are input through the keyboard.
#        Write an algorithm to calculate the area & perimeter of the rectangle, and the area &
#        circumference of the circle.
l=int(input("Length = "))
b=int(input("Breadth = "))
r=int(input("Radius = "))
ac=3.14*r*r
cc=2*3.14*r
ar=l*b;
pr=2*(l+b)
print("area of circle = ",ac)
print("circumference of circle = ",cc)
print("area of rectangle = ",ar)
print("Perimeter of rectangle = ",pr)
