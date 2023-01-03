#book
from tkinter import *
from tkinter.messagebox import askyesno,showinfo
import random
import sqlite3
#-------------------------------------
class journey:
    def __init__(self) :
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry("%dx%d+0+0"%(w,h))

        #img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\Bus_for_project.png")
        img=PhotoImage(file="project_resources/Bus_for_project.png")
        #img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\home.png")
        img2=PhotoImage(file="project_resources/home.png")

        #-----------Top Frame-----------------
        top_frame=Frame(root)
        top_frame.grid(row=0,column=2,padx=w//5)
        Label(top_frame,image=img).grid(pady=10)
        Label(top_frame,text="Online Bus Booking System",font="Ariel 18 bold ",bg='light blue',fg='red',relief="groove",bd=2).grid(pady=10)
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        #img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\home.png")
        self.img2=PhotoImage(file="project_resources/home.png")
        mid_frame=Frame(root)
        mid_frame.grid(row=2,column=2,padx=w//5,pady=20)
        Label(mid_frame,text="Enter Journey Details",font="Ariel 14 bold ",bg='light green',fg='green',relief="groove",bd=2).grid(row=2,column=0,columnspan=15,pady=10)
        Label(mid_frame,text="To",font="Ariel 12 bold ").grid(row=3,column=4)
        self.to=Entry(mid_frame,font="Ariel 12 bold ")
        self.to.grid(row=3,column=5)

        Label(mid_frame,text="From",font="Ariel 12 bold ").grid(row=3,column=6)
        self.fro=Entry(mid_frame,font="Ariel 12 bold ")
        self.fro.grid(row=3,column=7)
        
        Label(mid_frame,text="Journey Date",font="Ariel 12 bold ").grid(row=3,column=8)
        self.jdate=Entry(mid_frame,font="Ariel 12 bold ")
        self.jdate.grid(row=3,column=9)
            
        def home():
            root.destroy()
            from bbs_gui2 import home
            hm=home()
        Button(mid_frame,text="Show Bus",command=self.sel_bus,font="Ariel 12 bold ",bg='SpringGreen3',activebackground="SpringGreen3",bd=5).grid(row=3,column=10,padx=10)
        Button(mid_frame,image=self.img2,bd=3,command=home).grid(row=3,column=11,padx=10)
        root.mainloop()
    
    #-------------Select Bus---------------
    def sel_bus(self):
        select_bus=Frame()
        select_bus.grid(row=5,column=2,pady=20)
        bs=IntVar()
        n="1"
        #Radiobutton(select_bus,text="Bus ",value=1,indicator=0,font="Ariel 12 bold ",bg='light blue',activebackground="lime green").grid(row=6,column=2,padx=60)
        Label(select_bus,text="Select Bus",font="Ariel 12 bold ",fg='green').grid(row=5,column=2,padx=60)
        Label(select_bus,text="Opertor",font="Ariel 12 bold ",fg='green').grid(row=5,column=3,padx=60)
        Label(select_bus,text="Bus Type",font="Ariel 12 bold ",fg='green').grid(row=5,column=4,padx=60)
        Label(select_bus,text="Available/Capacity",font="Ariel 12 bold ",fg='green').grid(row=5,column=5,padx=60)
        Label(select_bus,text="Fare",font="Ariel 12 bold ",fg='green').grid(row=5,column=6,padx=60)
        Button(select_bus,text="Proceed to Book",command=self.book,font="Ariel 12 bold ",bg='lime green',activebackground="lime green",bd=3).grid(row=6,column=10,padx=60)

        self.to_st=self.to.get()
        self.source=self.fro.get()
        self.tr_on=self.jdate.get()
        con=sqlite3.connect("bbsdb.db")
        cur=con.cursor()
        #cur.execute('select distinct bid,r1.staid,r1.sta_name,r2.staid,r2.sta_name,run_date from route as r1,route as r2,run where (r1.sta_name="{0}" and r2.sta_name="{1}") and r1.staid>r2.staid and run_date="{2}";'.format(t,f,j))
        #cur.execute('select DISTINCT b.bid,oname,b.bus_type,seat_available,b.fare from operator,buses as b,route as r1,route as r2,run where (r1.sta_name="{0}" and r2.sta_name="{1}") and r1.staid>r2.staid and run_date="{2}" and b.rid=r2.rid;'.format(t,f,j))
        #cur.execute('select DISTINCT b.bid,oname,b.bus_type,seat_available,b.fare from operator,buses as b,route as r1,route as r2,run where (r1.sta_name="{0}" and r2.sta_name="{1}") and r1.staid>r2.staid and run_date="{2}" and b.rid=r2.rid; '.format(t,f,j))
        cur.execute('select DISTINCT b.bid,oname, b.bus_type,seat_available,b.fare from operator, buses as b,route as r1,route as r2,run where (r1.staid>r2.staid) and (r1.sta_name="{0}" and r2.sta_name="{1}") and (run_date="{2}") and (b.rid=r1.rid and run.bid=b.bid); '.format(self.to_st,self.source,self.tr_on))
        res=cur.fetchall()
        j=0
        for i in res:
            print(i[0],i[1],i[2],i[3],i[4])
            j+=1
            self.bus_no=IntVar()
            Radiobutton(select_bus,text="Bus"+str(j),value=j,indicator=0,font="Ariel 12 bold ",bg='light blue',activebackground="lime green").grid(row=6+j,column=2,padx=60)
            Label(select_bus,text=i[1],font="Ariel 12 bold ",fg='green').grid(row=6+j,column=3,padx=60)
            Label(select_bus,text=i[2],font="Ariel 12 bold ",fg='green').grid(row=6+j,column=4,padx=60)
            Label(select_bus,text=i[3],font="Ariel 12 bold ",fg='green').grid(row=6+j,column=5,padx=60)
            Label(select_bus,text=i[4],font="Ariel 12 bold ",fg='green').grid(row=6+j,column=6,padx=60)
        cur.close()
        con.close()


    #--------------Booking-----------------    
    def book(self):
        booking=Frame()
        booking.grid(row=10,column=2,pady=20)
        Label(booking,text="Fill Pasenger Details to book the bus ticket",font="Ariel 16 bold ",bg='light blue',fg='red',relief="groove",bd=2).grid(row=0,column=0,columnspan=15,pady=30)
        Label(booking,text="Name",font="Ariel 12 bold ").grid(row=2,padx=10, column=4)
        self.name=Entry(booking,font="Ariel 12 bold ")
        self.name.grid(row=2,padx=10, column=5)
        
        Label(booking,text="Gender",font="Ariel 12 bold ").grid(row=2,padx=10, column=6)
        self.gen=StringVar()
        opt=["Male","Female"]
        self.gen.set(opt[0])
        gen_menu=OptionMenu(booking,self.gen,*opt)
        gen_menu.config(font="Ariel 10 italic")
        
        gen_menu.grid(row=2,padx=10, column=7)

        Label(booking,text="No of Seats",font="Ariel 12 bold ").grid(row=2,padx=10, column=8)
        self.seats=Entry(booking,font="Ariel 12 bold ")
        self.seats.grid(row=2,padx=10, column=9)

        Label(booking,text="Mobile No ",font="Ariel 12 bold ").grid(row=2,padx=10, column=10)
        self.mob=Entry(booking,font="Ariel 12 bold ")
        self.mob.grid(row=2,padx=10, column=11)

        Label(booking,text="Age",font="Ariel 12 bold ").grid(row=2,padx=10, column=12)
        self.age=Entry(booking,font="Ariel 12 bold ")
        self.age.grid(row=2,padx=10, column=13)
        print(self.bus_no)

        Button(booking,text="Book Seat",font="Ariel 12 bold ",bg='light green',activebackground="light green",command=lambda:self.rec(self.bus_no),bd=3).grid(row=2,column=14,padx=10)
    def rec(self,x):
        n=self.name.get()
        g=self.gen.get()
        s=self.seats.get()
        m=self.mob.get()
        a=self.age.get()
        to=self.jdate.get()
        print(n,g,s,m,a)
        #try:
        bref=random.randint(1000000,9999999)
        print(bref)
        query='insert into pass_booking(book_ref,pname,gender,age,phone,seats,travel_on,booked_on) values({0},"{1}","{2}",{3},"{4}",{5},{6},DATE())'.format(bref,n,g,a,m,s,to)
        print(query)
        o=self.qx(query)
        if o==True and x==1:
            a=showinfo("Book Details","Booking record added Succesfully.")
            from bbs_gui4 import tic
            tk=tic(bref)
        elif o==True and x==2:
            a=showinfo("Book Details"," Booking Record Updated Succesfully.")
        else:
            raise Exception("Something went wrong.")
        #except:
        #    a=showinfo("Failure","    Operation Unsuccesful.\nMaybe Record already Exist or you have Entered Wrong Values.\n     Please try Again")

    def qx(self,query):
        con=sqlite3.Connection("bbsdb.db")
        cur=con.cursor()
        cur.execute(query)
        con.commit()
        cur.close()
        con.close()
        return True
    #-------------------------------------
jr=journey()
