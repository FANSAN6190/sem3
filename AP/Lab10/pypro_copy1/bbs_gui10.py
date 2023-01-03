from tkinter import *
from tkinter.messagebox import showinfo
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

#img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\Bus_for_project.png")
img=PhotoImage(file="AP/Lab10/project_resources/Bus_for_project.png")
#img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\home.png")
img2=PhotoImage(file="AP/Lab10/project_resources/home.png")

#---------------Frames-----------------
top_frame=Frame(root)
top_frame.grid(row=0,column=0,padx=w//5-150)

mid_frame=Frame(root)
mid_frame.grid(row=2,column=0,padx=w//5-150, pady=20)
#---------------------------------------
Label(top_frame,image=img).grid(pady=10)
Label(top_frame,text="Online Bus Booking System",font="Ariel 18 bold ",bg='light blue',fg='red').grid(pady=10)

Label(mid_frame,text="Add Bus Running Details",font="Ariel 16 bold ",fg='red',relief="raised").grid(columnspan=20,padx=200,pady=30)

Label(mid_frame,text="Bus id",font="Ariel 12 bold ").grid(row=2, column=2,padx=10)
name=Entry(mid_frame,font="Ariel 12 bold ")
name.grid(row=2, column=3)

Label(mid_frame,text="Running Date",font="Ariel 12 bold ").grid(row=2, column=4,padx=10)
jdate=Entry(mid_frame,font="Ariel 12 bold ")
jdate.grid(row=2, column=5)

Label(mid_frame,text="Seat Available",font="Ariel 12 bold ").grid(row=2, column=6,padx=10)
mob=Entry(mid_frame,font="Ariel 12 bold ")
mob.grid(row=2, column=7)

def conf():
    a=showinfo("operator entry","operator record added.")
Button(mid_frame,text="Add Run",font="Ariel 12 bold ",bg='light green',activebackground="light green",command=conf).grid(row=2,column=9,padx=20)
Button(mid_frame,text="Delete Run",font="Ariel 12 bold ",bg='light green',fg="red",activebackground="light green").grid(row=2,column=10,padx=20)
Button(mid_frame,image=img2).grid(row=3,column=8,pady=30)
root.mainloop()