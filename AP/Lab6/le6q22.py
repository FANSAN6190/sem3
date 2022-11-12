#22. Write a script to print all details of the student, asking user to keyin student’s name
from std import D1,D2,D3,D4,D5,D6
nm=input("Enter the Enrolment Number = ")
for i,j in D1.items():
    if j==nm:
        ern=i
print(ern,D1[ern],"  ",D2[ern],D3[ern],D4[ern],D5[ern],D6[ern])
