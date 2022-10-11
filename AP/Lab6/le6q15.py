#15. Write a python script to display students’ details who scored highest average marks in Phy, Chem, and Maths among all.
from std import D1,D2,D3,D4,D5,D6
q=[]
avg_mks=0
for i,j in D5.items():
    
    if j not in q:
        for k,l in D5.items():
            avm=(D5[k][0]+D5[k][1]+D5[k][2])/3
            if (avm>avg_mks):
                avg_mks=avm
count=0      
print("Highest Average Marks :",avg_mks)
for i in D5:
    if (D5[i][0]+D5[i][1]+D5[i][2])/3==avg_mks:
        count+=1
        st=[i,D1[i],D2[i],D3[i],D4[i],D5[i],D6[i]]
        print(count,st)
