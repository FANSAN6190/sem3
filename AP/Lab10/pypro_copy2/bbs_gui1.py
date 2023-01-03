#front
from tkinter import *

root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
#img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\Bus_for_project.png")
img=PhotoImage(file="AP/Lab10/project_resources/Bus_for_project.png")

def home(e):
    root.destroy()
    import bbs_gui2
root.bind("<Key>", home)
top_frame=Frame(root)
top_frame.grid(row=0,column=0,padx=w//3+125)

dev_info=Frame(root)
dev_info.grid(row=2,column=0,padx=w//3+125,pady=20)

Label(top_frame,image=img).grid(pady=10)
Label(top_frame,text="Online Bus Booking System",font="Ariel 18 bold ",bg='light blue',fg='red').grid(pady=10)

Label(dev_info,text="Name: Fanindra Saini",font="Ariel 12 bold ",fg='blue').grid(pady=40)
Label(dev_info,text="Er: 211B116",font="Ariel 12 bold ",fg='blue').grid()
Label(dev_info,text="Mobile: XXXXXXXXXX",font="Ariel 12 bold ",fg='blue').grid(pady=40)
Label(dev_info,text="Submitted to: Dr. Mahesh Kumar",font="Ariel 16 bold ",bg='powder blue',fg='red').grid()
Label(dev_info,text="Project Based Learning",font="Ariel 12 bold ",fg='red').grid()


#root.bind('<q>',home)
root.mainloop()
