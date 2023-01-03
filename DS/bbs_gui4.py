from tkinter import *
from tkinter import messagebox
import sqlite3
class tic:
    def __init__(self,brf):
        #fetching values of booking refrence brf 
        con=sqlite3.Connection('bbsdb.db')
        cur=con.cursor()
        cur.execute('select * from pass_booking where book_ref={0}'.format(brf))
        res=cur.fetchall()

        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry("%dx%d+0+0"%(w,h))
        #img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\Bus_for_project.png")
        img=PhotoImage(file="project_resources/Bus_for_project.png")
        messagebox.showinfo("Success","Seat Booked.....")
        top_frame=Frame(root)
        top_frame.grid(row=0,column=0,padx=w//3+125)

        ticket=Frame(root,relief="groove",borderwidth=5)
        ticket.grid(row=2,column=0,padx=w//3+125,pady=20)

        Label(top_frame,image=img).grid(pady=10)
        Label(top_frame,text="Online Bus Booking System",font="Ariel 18 bold ",bg='light blue',fg='red',relief="groove",bd=2).grid(pady=10)

        Label(top_frame,text="Bus Ticket",font="Ariel 10 bold").grid()
        Label(ticket,text="Passengers: "+res[0][1],font="Ariel 10 bold").grid(row=0,column=0)        
        Label(ticket,text="No of Seats: "+str(res[0][5]),font="Ariel 10 bold").grid(row=1,column=0)
        Label(ticket,text="Age:"+str(res[0][3]),font="Ariel 10 bold").grid(row=2,column=0)
        Label(ticket,text="Booking Ref.:"+str(res[0][0]),font="Ariel 10 bold").grid(row=3,column=0)
        Label(ticket,text="Travel On: "+res[0][6],font="Ariel 10 bold").grid(row=4,column=0)
        Label(ticket,text="No of Seats: "+str(res[0][5]),font="Ariel 10 bold").grid(row=5,column=0)
        Label(ticket,text="Gender: "+res[0][2],font="Ariel 10 bold").grid(row=0,column=2)
        Label(ticket,text="Phone: "+res[0][4],font="Ariel 10 bold").grid(row=1,column=2)
        Label(ticket,text="Fare Rs: "+str(res[0][10]),font="Ariel 10 bold").grid(row=2,column=2)
        Label(ticket,text="Bus Detail: "+str(res[0][9]),font="Ariel 10 bold").grid(row=3,column=2)
        Label(ticket,text="Booked On: "+res[0][7],font="Ariel 10 bold").grid(row=4,column=2)
        Label(ticket,text="Boarding Point: "+res[0][8],font="Ariel 10 bold").grid(row=5,column=2)
        
        Label(ticket,text="*Total amount Rs."+"/- to be paid at the time of boarding bus",font="Ariel 8").grid()
        def on_closing():
            mess=messagebox.askyesnocancel("quit","do you want to quit")
            if mess:
                print(mess)
                root.destroy()
            elif mess=="None":
                print(mess)
            else:
                root.destroy()
                import bbs_gui2
        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.mainloop()
tc=tic(1589455)