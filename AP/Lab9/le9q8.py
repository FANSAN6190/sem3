#9. Write a python script that creates a GUI with a single button. When the button is pressed it should create a second button. When that button is pressed, it should create a label that says, “Nice job!”. What happens if you press the buttons more than once?
from tkinter import *
root=Tk()
def event():
    Label(root,text="Nice job!").pack()
def new_button():
    Button(root,text="Press2",command=event).pack()
Button(root,text="Press1",command=new_button).pack()
root.mainloop()
