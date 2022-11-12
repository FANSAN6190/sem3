#10. Write a python script to display students’ details who have email id on same host (i.e. gmail.com,
#    yahoo.com, rediffmail.com etc )
from std import D1,D2,D3,D4,D5,D6
q=[]
for i,j in D6.items():
    lis=j.split("@")
    j=lis[1]
    count=0
    if j not in q:
        print("Students from ",j," -")
        for k,l in D6.items():
            lis=l.split("@")
            l=lis[1]
            if j==l:
                count+=1
                st=[k,D1[k],D2[k],D3[k],D4[k],D5[k],D6[k]]
                print(count,st)
                q.append(l)
        print("\n")
