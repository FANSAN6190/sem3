#12. Write a python script to display students’ details who scored highest marks in Phy among all.
from std import D1,D2,D3,D4,D5,D6
q=[]
phy_mks=0
for i,j in D5.items():
    
    if j not in q:
        for k,l in D5.items():
            if (D5[k][0]>phy_mks):
                phy_mks=D5[k][0]
count=0      
print("Highest Physics Marks :",phy_mks)
for i in D5:
    if D5[i][0]==phy_mks:
        count+=1
        st=[i,D1[i],D2[i],D3[i],D4[i],D5[i][0],D6[i]]
        print(count,st)
