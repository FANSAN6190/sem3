##P3. Write a python function to check whether three given numbers can form the sides of a
##triangle.
##Hint: Three numbers can be the sides of a triangle if none of the numbers are greater than or
##equal to the sum of the other two numbers.
def tri(s1,s2,s3):
    if s1>(s2+s3):
        print("Invalid Triangle")
    elif s2>(s1+s3):
        print("Invalid Triangle")
    elif s3>(s1+s2):
        print("Invalid Triangle")
    else:
        print("Valid Triangle")
s1=int(input("Enter the length of side1 = "))
s2=int(input("Enter the length of side2 = "))
s3=int(input("Enter the length of side3 = "))
tri(s1,s2,s3)
