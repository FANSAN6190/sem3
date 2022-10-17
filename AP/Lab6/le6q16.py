#16. Write a python script to create a dictionary square to store 10 integers and their square
square={}
for i in range(1,11):
    square.update({i:i*i})
print(square)
