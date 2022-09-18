#D. Write a function named rightjustify that takes a string named s as a parameter and prints the string with enough leading spaces
hs=20
def rightjustify(i):
    l=len(i)
    return " "*(20-l)+i
s=""
print("Enter the String : ")
for i in iter(input,s):
    if i=='0':
        break
    s=s+rightjustify(i)+'\n'
print(s)
