#H. Calculate number of occurrences of 'a' in a input string using recursion.
def stc(st,i,a):
    if st[i]=='a':
        a+=1
    elif st[i]=='\0':
        return;
    i+=1
    stc(st,i,a)
a=0
st=input("Enter the String = ")
stc(st,0,a)
print(a)
