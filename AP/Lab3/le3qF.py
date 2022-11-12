#F. Write a function to print number 1 to 10 in ascending or descending order, based on user choice.
ch=input("Enter the Choice (A ,D) = ")
if(ch=='A'):
    for i in range(1,11):
        print(i)
elif(ch=='D'):
    for i in range(10,0,-1):
        print(i)
else:
    print("Wrong Input")
