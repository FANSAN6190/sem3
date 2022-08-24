#15: If a five-digit number is input through the keyboard, write a python program to print a new
#      number by adding one to each of it digits. For example if the number that is input is 12391
#      then the output should be displayed as 23402. [If digit is 9 it should be converted into 0].
n=int(input("Enter the number = "))
m=0
while n!=0:
    r=n%10+1
    n=n//10
    if(r==10):
        r=0
    m=r+(m*10)
    
print("New Number = ",m)
