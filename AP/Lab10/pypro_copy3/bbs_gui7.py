from tkinter import *
from tkinter.messagebox import showinfo
import sqlite3
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

#img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\Bus_for_project.png")
img=PhotoImage(file="project_resources/Bus_for_project.png")
#img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\home.png")
img2=PhotoImage(file="project_resources/home.png")

#---------------Frames-----------------
top_frame=Frame(root)
top_frame.grid(row=0,column=0,padx=w//5-225)
Label(top_frame,image=img).grid(pady=10)
Label(top_frame,text="Online Bus Booking System",font="Ariel 18 bold ",bg='light blue',fg='red').grid(pady=10)

#def mid_frame_content():
mid_frame=Frame(root)
mid_frame.grid(row=2,column=0,padx=w//5-225,pady=20)
Label(mid_frame,text="Add Bus Operator Details",font="Ariel 16 bold ",fg='red',relief="raised").grid(columnspan=20,pady=30)

Label(mid_frame,text="Operator id",font="Ariel 12 bold ").grid(row=2, column=0)
oid=Entry(mid_frame,font="Ariel 12 bold ")
oid.grid(row=2, column=1)

Label(mid_frame,text="Name",font="Ariel 12 bold ").grid(row=2, column=2)
name=Entry(mid_frame,font="Ariel 12 bold ")
name.grid(row=2, column=3)

Label(mid_frame,text="Address",font="Ariel 12 bold ").grid(row=2, column=4)
address=Entry(mid_frame,font="Ariel 12 bold ")
address.grid(row=2, column=5)

Label(mid_frame,text="Phone ",font="Ariel 12 bold ").grid(row=2, column=6)
phone=Entry(mid_frame,font="Ariel 12 bold ")
phone.grid(row=2, column=7)

Label(mid_frame,text="Email",font="Ariel 12 bold ").grid(row=2, column=8)
email=Entry(mid_frame,font="Ariel 12 bold ")
email.grid(row=2, column=9)

def rec(x):
    o=oid.get()
    n=name.get()
    a=address.get()
    p=phone.get()
    e=email.get()
    
    #try:
    if x==1:
        query='insert into operator (oid,oname,phone,email,address) values({0},"{1}","{2}","{3}","{4}")'.format(o,n,p,e,a)
    elif x==2:
        query='update operator set oid={0},oname="{1}",phone="{2}",email="{3}",address="{4}"'.format(o,n,a,p,e)
    o=qx(query)
    if o==True and x==1:
        a=showinfo("Operator Details","Operator record added Succesfully.")
    elif o==True and x==2:
        a=showinfo("Operators Details","Operator Record Updated Succesfully.")
    else:
        raise Exception("Something went wrong.")
    #except:
    #    a=showinfo("Failure","    Operation Unsuccesful.\nMaybe Record already Exist or you have Entered Wrong Values.\n     Please try Again")
        
def qx(query):
    con=sqlite3.Connection('bbsdb.db')
    cur=con.cursor()
    cur.execute(query)  
    con.commit()
    cur.close()
    con.close()
    return True
    
Button(mid_frame,text="Add",font="Ariel 12 bold ",bg='light green',activebackground="light green",command=lambda:rec(1)).grid(row=2,column=14)
Button(mid_frame,text="Edit",font="Ariel 12 bold ",bg='light green',activebackground="light green",command=lambda:rec(2)).grid(row=2,column=15)
root.mainloop()