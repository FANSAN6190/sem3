#book
from tkinter import *
from tkinter.messagebox import askyesno
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

#img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\Bus_for_project.png")
img=PhotoImage(file="AP/Lab10/project_resources/Bus_for_project.png")
#img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\home.png")
img2=PhotoImage(file="AP/Lab10/project_resources/home.png")

#--------------Booking-----------------    
def book():
    booking=Frame(root)
    booking.grid(row=10,column=2,pady=20)
    Label(booking,text="Fill Pasenger Details to book the bus ticket",font="Ariel 16 bold ",bg='light blue',fg='red',relief="groove",bd=2).grid(row=0,column=0,columnspan=15,pady=30)
    Label(booking,text="Name",font="Ariel 12 bold ").grid(row=2,padx=10, column=4)
    name=Entry(booking,font="Ariel 12 bold ")
    name.grid(row=2,padx=10, column=5)

    Label(booking,text="Gender",font="Ariel 12 bold ").grid(row=2,padx=10, column=6)
    gen=StringVar()
    opt=["Male","Female"]
    gen.set(opt[0])
    gen_menu=OptionMenu(booking,gen,*opt)
    gen_menu.config(font="Ariel 10 italic")
    
    gen_menu.grid(row=2,padx=10, column=7)

    Label(booking,text="No of Seats",font="Ariel 12 bold ").grid(row=2,padx=10, column=8)
    jdate=Entry(booking,font="Ariel 12 bold ")
    jdate.grid(row=2,padx=10, column=9)

    Label(booking,text="Mobile No ",font="Ariel 12 bold ").grid(row=2,padx=10, column=10)
    mob=Entry(booking,font="Ariel 12 bold ")
    mob.grid(row=2,padx=10, column=11)

    Label(booking,text="Age",font="Ariel 12 bold ").grid(row=2,padx=10, column=12)
    age=Entry(booking,font="Ariel 12 bold ")
    age.grid(row=2,padx=10, column=13)

    def conf():
        a=askyesno("choice","Total amount to be Paid is ")
    Button(booking,text="Book Seat",font="Ariel 12 bold ",bg='light green',activebackground="light green",command=conf,bd=3).grid(row=2,column=14,padx=10)
#-------------------------------------

#-------------Select Bus---------------
def sel_bus():
    select_bus=Frame(root)
    select_bus.grid(row=5,column=2,pady=20)
    bs=IntVar()
    n="1"
    Radiobutton(select_bus,text="Bus ",value=1,indicator=0,font="Ariel 12 bold ",bg='light blue',activebackground="lime green").grid(row=6,column=2,padx=60)
    Label(select_bus,text="Select Bus",font="Ariel 12 bold ",fg='green').grid(row=5,column=2,padx=60)
    Label(select_bus,text="Opertor",font="Ariel 12 bold ",fg='green').grid(row=5,column=3,padx=60)
    Label(select_bus,text="Bus Type",font="Ariel 12 bold ",fg='green').grid(row=5,column=4,padx=60)
    Label(select_bus,text="Available/Capacity",font="Ariel 12 bold ",fg='green').grid(row=5,column=5,padx=60)
    Label(select_bus,text="Fare",font="Ariel 12 bold ",fg='green').grid(row=5,column=6,padx=60)
    Button(select_bus,text="Proceed to Book",command=book,font="Ariel 12 bold ",bg='lime green',activebackground="lime green",bd=3).grid(row=6,column=10,padx=60)
#--------------------------------------

#-----------Top Frame-----------------
top_frame=Frame(root)
top_frame.grid(row=0,column=2,padx=w//5)
Label(top_frame,image=img).grid(pady=10)
Label(top_frame,text="Online Bus Booking System",font="Ariel 18 bold ",bg='light blue',fg='red',relief="groove",bd=2).grid(pady=10)
#-------------------------------------

#-----------Mid Frame-----------------
mid_frame=Frame(root)
mid_frame.grid(row=2,column=2,padx=w//5,pady=20)
Label(mid_frame,text="Enter Journey Details",font="Ariel 14 bold ",bg='light green',fg='green',relief="groove",bd=2).grid(row=2,column=0,columnspan=15,pady=10)

Label(mid_frame,text="To",font="Ariel 12 bold ").grid(row=3,column=4)
to=Entry(mid_frame,font="Ariel 12 bold ")
to.grid(row=3,column=5)

Label(mid_frame,text="From",font="Ariel 12 bold ").grid(row=3,column=6)
fro=Entry(mid_frame,font="Ariel 12 bold ")
fro.grid(row=3,column=7)

Label(mid_frame,text="Journey Date",font="Ariel 12 bold ").grid(row=3,column=8)
jdate=Entry(mid_frame,font="Ariel 12 bold ")
jdate.grid(row=3,column=9)

def home():
    root.destroy()
    import bbs_gui2

Button(mid_frame,text="Show Bus",command=sel_bus,font="Ariel 12 bold ",bg='SpringGreen3',activebackground="SpringGreen3",bd=5).grid(row=3,column=10,padx=10)
Button(mid_frame,image=img2,bd=3,command=home).grid(row=3,column=11,padx=10)
#-------------------------------------

root.mainloop()