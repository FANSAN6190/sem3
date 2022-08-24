#17. Write a program to prints the integer cube root, if it exists, of an integer. If the input is not a
#    perfect cube, it prints a message “the number is not perfect cube” otherwise it prints “the number is
#    perfect cube”.
n=int(input(" "))
r=round(n**(1/3))
if r**3==n:
    print("The number is perfect cube. ",r)
else:
    print("The number is not perfect cube.")
