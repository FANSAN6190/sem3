#7. Write a python script to read First Name and Last Name using text boxes, Wish the user with the first name “ ….name…. Welcome to Python”
from tkinter import *
root=Tk()
first_name=Entry(root)
first_name.pack()
last_name=Entry(root)
last_name.pack()
def event():
    Label(root,text="Welcome...."+first_name.get()+" "+last_name.get()).pack()
Button(root,text="GO",command=event).pack()
root.mainloop()

