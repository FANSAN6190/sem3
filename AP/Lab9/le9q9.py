#10. Write a python script to computer simple interest on the root window.
from tkinter import *
root=Tk()
Label(root,text="Enter the Principle Amount").pack()
principle=Entry(root)
principle.pack()
Label(root,text="Enter the Rate of Intrest").pack()
rate=Entry(root)
rate.pack()
Label(root,text="Enter the Time in Years").pack()
time=Entry(root)
time.pack()
def sim_int():
    si=int(principle.get())*int(rate.get())*int(time.get())/100
    Label(root,text="Simple Intrest = "+str(si)).pack()
Button(root,text="Calculate",command=sim_int).pack()
root.mainloop()
