##Prob3: Read a list from the user of arbitrary length, and show following:
## print the list entered by the user
## print least value and largest value
## swap positions of least and largest element
## print the list after swapping positions.
li=[]
n=int(input("Enter the range = "))
for i in range(0,n):
    a=int(input())
    li.append(a)
print(li)
mx=mn=li[0]
for i in li:
    if i>mx:
        mx=i
    elif i<mn:
        mn=i
print(mx," ",mn)
i=0
for i in range(0,n):
    if li[i]==mx:
        li[i]=mn
    elif li[i]==mn:
        li[i]=mx
print(li)

