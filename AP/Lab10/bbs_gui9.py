from tkinter import *
from tkinter.messagebox import showinfo
import sqlite3
class route:
    def __init__(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry("%dx%d+0+0"%(w,h))
        img=PhotoImage(file="project_resources/Bus_for_project.png")
        img2=PhotoImage(file="project_resources/home.png")
        top_frame=Frame(root)
        top_frame.grid(row=0,column=0,padx=w//5-150)
        mid_frame=Frame(root)
        mid_frame.grid(row=2,column=0,padx=w//5-150, pady=20)
        Label(top_frame,image=img).grid(pady=10)
        Label(top_frame,text="Online Bus Booking System",font="Ariel 18 bold ",bg='light blue',fg='red').grid(pady=10)
        Label(mid_frame,text="Add Bus Route Details",font="Ariel 16 bold ",fg='red',relief="raised").grid(columnspan=20,padx=200,pady=30)
        Label(mid_frame,text="Route id",font="Ariel 12 bold ").grid(row=2, column=2,padx=10)
        self.rid=Entry(mid_frame,font="Ariel 12 bold ")
        self.rid.grid(row=2, column=3)
        Label(mid_frame,text="Station Name",font="Ariel 12 bold ").grid(row=2, column=4,padx=10)
        self.st_name=Entry(mid_frame,font="Ariel 12 bold ")
        self.st_name.grid(row=2, column=5)
        Label(mid_frame,text="Station ID",font="Ariel 12 bold ").grid(row=2, column=6,padx=10)
        self.st_id=Entry(mid_frame,font="Ariel 12 bold ")
        self.st_id.grid(row=2, column=7)
        Button(mid_frame,text="Add Route",font="Ariel 12 bold ",bg='light green',activebackground="light green",command=lambda:self.rec(1)).grid(row=2,column=9,padx=20)
        Button(mid_frame,text="Delete Route",font="Ariel 12 bold ",bg='light green',fg="red",activebackground="light green",command=lambda:self.rec(3)).grid(row=2,column=10,padx=20)
        def home():
            root.destroy()
            from bbs_gui2 import home
            hm=home()
        Button(mid_frame,image=img2,command=home).grid(row=3,column=8,pady=30)
        root.mainloop()
    def rec(self,x):
        r=self.rid.get()
        stid=self.st_id.get()
        stn=self.st_name.get()
        if x==1:
            query='insert into route(rid,staid,sta_name) values({0},{1},"{2}") '.format(r,stid,stn)
        elif x==3:
            query=' delete from route where rid={0} and staid={1} and sta_name="{2}" '.format(r,stid,stn)
        print(query)
        o=self.qx(query)
        if o==True and x==1:
            a=showinfo("Route","record added Succesfully.")
        elif o==True and x==3:
            a=showinfo("Route"," Record deleated Succesfully.")
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
