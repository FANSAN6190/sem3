#11: If the marks obtained by a student in five different subjects are input through the keyboard,
#      find out the aggregate marks and percentage marks obtained by the student. Assume that
#      the maximum marks that can be obtained by a student in each subject is 100.
print("Enter marks out of 100")
a=int(input("s1="))
b=int(input("s2="))
c=int(input("s3="))
d=int(input("s4="))
e=int(input("s5="))
agm=(a+b+c+d+e)/5
pc=(a+b+c+d+e)*100/(5*100)
print("Agregate marks  = ",agm,"   Percentage = ",pc)
