from tkinter import *
from tkinter.messagebox import showinfo
import sqlite3
class bus:
    def __init__(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry("%dx%d+0+0"%(w,h))

        #img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\Bus_for_project.png")
        img=PhotoImage(file="project_resources/Bus_for_project.png")
        #img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\home.png")
        img2=PhotoImage(file="project_resources/home.png")

        #---------------Frames-----------------
        top_frame=Frame(root)
        top_frame.grid(row=0,column=0,padx=w//5-100)

        mid_frame=Frame(root)
        mid_frame.grid(row=2,column=0,padx=100, pady=20)

        Label(top_frame,image=img).grid(pady=10)
        Label(top_frame,text="Online Bus Booking System",font="Ariel 18 bold ",bg='light blue',fg='red').grid(pady=10)


        Label(mid_frame,text="Add Bus Details",font="Ariel 16 bold ",fg='red',relief="raised").grid(row=0,column=0,columnspan=20,padx=200,pady=30)

        Label(mid_frame,text="Bus id",font="Ariel 12 bold ").grid(row=2, column=4)
        self.bid=Entry(mid_frame,font="Ariel 12 bold ")
        self.bid.grid(row=2, column=5)

        Label(mid_frame,text="Bus Type",font="Ariel 12 bold ").grid(row=2,padx=10, column=6)
        self.bus_type=StringVar()
        opt=["AC 2X2","AC 3X2","Non AC 2X2","Non AC 3X2","AC-Sleeper 2x1","Non-AC Sleeper 2x1"]
        self.bus_type.set(opt[0])
        bus_type_menu=OptionMenu(mid_frame,self.bus_type,*opt)
        bus_type_menu.grid(row=2,padx=10, column=7)

        Label(mid_frame,text="Capacity",font="Ariel 12 bold ").grid(row=2, column=8)
        self.capacity=Entry(mid_frame,font="Ariel 12 bold ")
        self.capacity.grid(row=2, column=9)

        Label(mid_frame,text="Fare Rs",font="Ariel 12 bold ").grid(row=2, column=10)
        self.fare=Entry(mid_frame,font="Ariel 12 bold ")
        self.fare.grid(row=2, column=11)

        Label(mid_frame,text="Operator ID",font="Ariel 12 bold ").grid(row=2, column=12)
        self.oid=Entry(mid_frame,font="Ariel 12 bold ")
        self.oid.grid(row=2, column=13)

        Label(mid_frame,text="Route id",font="Ariel 12 bold ").grid(row=2, column=14)
        self.rid=Entry(mid_frame,font="Ariel 12 bold ")
        self.rid.grid(row=2, column=15)
        Button(mid_frame,text="Add Bus",font="Ariel 12 bold ",bg='light green',activebackground="light green",command=lambda:self.rec(1)).grid(row=3,column=9,pady=30)
        Button(mid_frame,text="Edit Bus",font="Ariel 12 bold ",bg='light green',activebackground="light green",command=lambda:self.rec(2)).grid(row=3,column=10,pady=30)
        def home():
            root.destroy()
            from bbs_gui2 import home
            hm=home()
        Button(mid_frame,image=img2,command=home).grid(row=3,column=11,pady=30)
        root.mainloop()
        #-----------------------------------
    
    def rec(self,x):
        n=self.bid.get()
        o=self.oid.get()
        r=self.rid.get()
        bt=self.bus_type.get()
        c=self.capacity.get()
        f=self.fare.get()
        try:
            if x==1:
                query='insert into buses(bid,oid,rid,bus_type,capacity,fare) values("{0}",{1},{2},"{3}",{4},{5})'.format(n,o,r,bt,c,f)
            elif x==2:
                query='update buses set bid="{0}",oid={1},rid={2},bus_type="{3}",capacity={4},fare={5} where bid="{0}"'.format(n,o,r,bt,c,f)
            print(query)
            o=self.qx(query)
            if o==True and x==1:
                a=showinfo("Bus Details","Bus record added Succesfully.")
            elif o==True and x==2:
                a=showinfo("Bus Details"," Bus Record Updated Succesfully.")
            else:
                raise Exception("Something went wrong.")
        except:
            a=showinfo("Failure","    Operation Unsuccesful.\nMaybe Record already Exist or you have Entered Wrong Values.\n     Please try Again")

    def qx(self,query):
        con=sqlite3.Connection("bbsdb.db")
        cur=con.cursor()
        cur.execute(query)
        con.commit()
        cur.close()
        con.close()
        return True
    #--------------------------------------
#ab=bus()