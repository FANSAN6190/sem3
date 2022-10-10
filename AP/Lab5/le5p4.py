##Prob4: Read two lists enrol and name from the user of 10 elements. The list enrol contains
##enrolment numbers and list name contains names of the students. Now read enrolment
##number from the user to search in the list, if the enrolment is found in the list then print
##enrolment and name of the student. Otherwise print -1.
enrol=["211b001","211b002","211b003"]
name=["asdf","gsdfg","wtrrqr"]
ern=input("Enter the Enrollment Number = ")
p=0
for i in range(0,3):
    if ern==enrol[i]:
        print(enrol[i],"  ",name[i])
        p=1
        break
if(p==0):
    print(-1)
 