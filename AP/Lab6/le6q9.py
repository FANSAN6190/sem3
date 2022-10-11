#9. Write a python script to display students’ details who are from same State.
from std import D1,D2,D3,D4,D5,D6
q=[]
for i,j in D4.items():
    count=0
    if j not in q:
        print("Students from ",j," -")
        for k,l in D4.items():
            if j==l:
                count+=1
                st=[k,D1[k],D2[k],D3[k],D5[k],D6[k]]
                print(count,st)
                q.append(l)
        print("\n")