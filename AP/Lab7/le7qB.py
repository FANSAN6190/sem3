#B. Write a program to count number of words in string.
st="""Write a program to count number of words in string."""
w=0
for i in st:
    if i==' ' or i=='\n':
        w+=1;
print(w+1)
