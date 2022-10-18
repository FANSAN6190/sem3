#P4. Execute the program triangle.py available in the folder. The program triangle.py is
#written to display “*” as per the expected output given below. But the code is having logical
#errors, debug the program and correct it.
counter1=0
while counter1<5:
    star=""
    counter2=5
    while counter2>counter1:
        star=star+"*"
        counter2-=1
    print(star)
    counter1+=1
    
        
