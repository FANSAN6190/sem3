#13. Write a python script to display students’ details who scored highest marks in Chem among all
from std import D1,D2,D3,D4,D5,D6
q=[]
chem_mks=0
for i,j in D5.items():
    
    if j not in q:
        for k,l in D5.items():
            if (D5[k][1]>chem_mks):
                chem_mks=D5[k][1]
count=0      
print("Highest chemistry Marks :",chem_mks)
for i in D5:
    if D5[i][1]==chem_mks:
        count+=1
        st=[i,D1[i],D2[i],D3[i],D4[i],D5[i][1],D6[i]]
        print(count,st)

