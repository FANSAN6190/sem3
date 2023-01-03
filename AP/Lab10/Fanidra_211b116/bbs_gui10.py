from tkinter import *
from tkinter.messagebox import showinfo
import sqlite3
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
class run:
    def __init__(self):
        #img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\Bus_for_project.png")
        img=PhotoImage(file="project_resources/Bus_for_project.png")
        #img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\home.png")
        img2=PhotoImage(file="project_resources/home.png")

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
        self.bid=Entry(mid_frame,font="Ariel 12 bold ")
        self.bid.grid(row=2, column=3)

        Label(mid_frame,text="Running Date",font="Ariel 12 bold ").grid(row=2, column=4,padx=10)
        self.rdate=Entry(mid_frame,font="Ariel 12 bold ")
        self.rdate.grid(row=2, column=5)

        Label(mid_frame,text="Seat Available",font="Ariel 12 bold ").grid(row=2, column=6,padx=10)
        self.savail=Entry(mid_frame,font="Ariel 12 bold ")
        self.savail.grid(row=2, column=7)

        Button(mid_frame,text="Add Run",font="Ariel 12 bold ",bg='light green',activebackground="light green",command=lambda:self.rec(1)).grid(row=2,column=9,padx=20)
        Button(mid_frame,text="Delete Run",font="Ariel 12 bold ",bg='light green',fg="red",activebackground="light green",command=lambda:self.rec(3)).grid(row=2,column=10,padx=20)

        def home():
            root.destroy()
            from bbs_gui2 import home
            hm=home()
        Button(mid_frame,image=img2,command=home).grid(row=3,column=8,pady=30)
        root.mainloop()

    def rec(self,x):
        id=self.bid.get()
        seat_avail=self.savail.get()
        rdt=self.rdate.get()
        if x==1:
            query='insert into run(bid,seat_available,run_date) values("{0}",{1},"{2}") '.format(id,seat_avail,rdt)    
        elif x==3:
            query=' delete from run where bid="{0}" and run_date="{1}"'.format(id,rdt)
        print(query)
        o=self.qx(query)
        if o==True and x==1:
            a=showinfo("Run","record added Succesfully.")
        elif o==True and x==3:
            a=showinfo("Run"," Record deleated Succesfully.")
        else:
            print("Something Went Wrong")
        

    def qx(self,query):
        con=sqlite3.connect("bbsdb.db")
        cur=con.cursor()
        cur.execute(query)
        con.commit()
        cur.close()
        con.close()
        return True
#rn=run()