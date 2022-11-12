#17. Write a python script to create any data structure named sroot to store 10 integers between 20 and 30,their square root.
sqroot={}
for i in range(20,31):
    sqroot.update({i:i**(1/2)})
print(sqroot)
