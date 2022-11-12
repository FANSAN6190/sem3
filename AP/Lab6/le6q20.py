#20. Write a script to print selected details of the student, asking user to key in student’s name
from std import D1,D2,D3,D4,D5,D6
nm=input("Enter the Name = ")
details=input("Enter the details you want as\n\nadd for city,state\nphn for phone No.\neml for email\nmks for marks \n= ").split(" ")
ern=0
for i,j in D1.items():
    if j==nm:
        ern=i
print("\n| ",ern,end=" | ")
if 'add' in details:
    print(D2[ern]+","+D4[ern],end=" | ")
if 'phn' in details:
    print(D3[ern],end=" | ")
if 'eml' in details:
    print(D6[ern],end=" | ")
if 'mks' in details:
    print(D5[ern],end=" | ")
print("\n")