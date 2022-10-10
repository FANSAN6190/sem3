#8.a. Write a python script to display students’ name and email by receiving enrolment number at run time.
from std import D1,D2,D3,D4,D5,D6;
a=int(input("Enter the ERN = "))
print(D1[a]," : ",D6[a])

###8.b. Write a python script to print name and enrolment number of the student by receiving email id at run time.
##eid=input("Enter the Email-ID = ")
##for i,j in D6.items():
##    if j==eid:
##        print(i)
##
###8.c. Write a python script to print name and city of the student by mobile number at run time.
##mn=input("Enter the Mobile No = ")
##for i,j in D3.items():
##    if j==mn:
##        print(D1[i]," : ",D2[i])


#8.d Write a python script to display students’ details who are from same hometown.

for i,j in D2.items():
    print("Students from ",j)
    for m,n in D2.items():
        if j==n:
            print(m,D1[m],D2[m],D3[m],D4[m],D5[m],D6[m])

