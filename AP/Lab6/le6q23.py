#23. Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the list.
i=0
y=int(input("Enter the Year = "))
y_lis=[]
while(i<15):
    if y%4==0 and y%100!=0 or y%400==0:
        y_lis.append(y)
        i+=1
    y+=1
print(y_lis)
    