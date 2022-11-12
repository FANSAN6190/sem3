#5. Write a python script to add event to the button added in previous problem and add string “Welcome....” to button event to the root window
from tkinter import *
root=Tk()
def event():
    Label(root,text="Welcome....").pack()
Button(root,text="GO",command=event).pack()
root.mainloop()
