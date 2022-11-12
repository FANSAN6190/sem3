#E. Write a program to find a substring within a string. If found display its starting position.
st=input("Enter the Main String = ")
ss=input("Enter the Sub String =")

if ss in st:
    print("String Found at = ",st.index(ss))
else:
    print("String Not Found")
