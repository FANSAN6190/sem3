#8. Write a python script to read two numbers and print their Sum/ Diff/ Multiplication/ Div/ Remainder on screen, using button for each operation.
from tkinter import *
root=Tk()
Label(root,text="Enter the First Number : ").pack()
num1=Entry(root)
num1.pack()
Label(root,text="Enter the Second Number : ").pack()
num2=Entry(root)
num2.pack()
####
def SUM():
    print(int(num1.get())+int(num2.get()))
def DIFF():
    print(int(num1.get())-int(num2.get()))
def MUL():
    print(int(num1.get())*int(num2.get()))
def DIV():
    print(int(num1.get())/int(num2.get()))
def REM():
    print(int(num1.get())%int(num2.get()))
####
Button(root,text="Sum",command=SUM).pack()
Button(root,text="Difference",command=DIFF).pack()
Button(root,text="Multiplication",command=MUL).pack()
Button(root,text="Division",command=DIV).pack()
Button(root,text="Remainder",command=REM).pack()
root.mainloop()

