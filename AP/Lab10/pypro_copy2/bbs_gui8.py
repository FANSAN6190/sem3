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
top_frame.grid(row=0,column=0,padx=w//5-100)

mid_frame=Frame(root)
mid_frame.grid(row=2,column=0,padx=100, pady=20)

Label(top_frame,image=img).grid(pady=10)
Label(top_frame,text="Online Bus Booking System",font="Ariel 18 bold ",bg='light blue',fg='red').grid(pady=10)


Label(mid_frame,text="Add Bus Details",font="Ariel 16 bold ",fg='red',relief="raised").grid(row=0,column=0,columnspan=20,padx=200,pady=30)

Label(mid_frame,text="Bus id",font="Ariel 12 bold ").grid(row=2, column=4)
name=Entry(mid_frame,font="Ariel 12 bold ")
name.grid(row=2, column=5)

Label(mid_frame,text="Bus Type",font="Ariel 12 bold ").grid(row=2,padx=10, column=6)
gen=StringVar()
opt=["AC 2X2","AC 3X2","Non AC 2X2","Non AC 3X2","AC-Sleeper 2x1","Non-AC Sleeper 2x1"]
gen.set(opt[0])
gen_menu=OptionMenu(mid_frame,gen,*opt)
gen_menu.grid(row=2,padx=10, column=7)

Label(mid_frame,text="Capacity",font="Ariel 12 bold ").grid(row=2, column=8)
jdate=Entry(mid_frame,font="Ariel 12 bold ")
jdate.grid(row=2, column=9)

Label(mid_frame,text="Fare Rs",font="Ariel 12 bold ").grid(row=2, column=10)
jdate=Entry(mid_frame,font="Ariel 12 bold ")
jdate.grid(row=2, column=11)

Label(mid_frame,text="Operator ID",font="Ariel 12 bold ").grid(row=2, column=12)
mob=Entry(mid_frame,font="Ariel 12 bold ")
mob.grid(row=2, column=13)

Label(mid_frame,text="Route id",font="Ariel 12 bold ").grid(row=2, column=14)
age=Entry(mid_frame,font="Ariel 12 bold ")
age.grid(row=2, column=15)

def conf():
    a=showinfo("operator entry","operator record added.")
Button(mid_frame,text="Add Bus",font="Ariel 12 bold ",bg='light green',activebackground="light green",command=conf).grid(row=3,column=9,pady=30)
Button(mid_frame,text="Edit Bus",font="Ariel 12 bold ",bg='light green',activebackground="light green").grid(row=3,column=10,pady=30)

def home():
    root.destroy()
    import bbs_gui2
Button(mid_frame,image=img2,command=home).grid(row=3,column=11,pady=30)
root.mainloop()