#11. Write a python script to display students’ details whose mobile service provider is same
#    (first two bits 94:BSNL, 98: Airtel, 89:Idea, 77:Reliance, 97:Idea, 99:Vodafone, 79:Docomo)
from std import D1,D2,D3,D4,D5,D6
q=[]
for i,j in D3.items():
    count=0
    j=j[0]+j[1]
    if j not in q:
        com_dict={"94":"BSNL","98":" Airtel","89":"Idea","77":"Reliance","97":"Idea","99":"Vodafone","79":"Docomo"}
        if j in com_dict.keys():
            print("Service Providers: ",com_dict[j],"")
        else:
            print("Others - ",j)
        for k,l in D3.items():
            l=l[0]+l[1]
            if j==l:
                count+=1
                st=[k,D1[k],D2[k],D3[k],D5[k],D6[k]]
                print(count,st)
                q.append(l)
        print("\n")