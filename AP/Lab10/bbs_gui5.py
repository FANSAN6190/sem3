from tkinter import *
from tkinter import messagebox
import sqlite3
class cyb:
    def __init__(self):
        root=Tk()
        w,h=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry("%dx%d+0+0"%(w,h))
        img=PhotoImage(file="project_resources/Bus_for_project.png")
        img2=PhotoImage(file="project_resources/home.png")
        top_frame=Frame(root)
        top_frame.grid(row=0,column=0,padx=w//3)
        booking=Frame(root)
        booking.grid(row=2,column=0,padx=w//3,pady=20)
        Label(top_frame,image=img).grid(pady=10)
        Label(top_frame,text="Online Bus Booking System",font="Ariel 18 bold ",bg='light blue',fg='red',relief="raised").grid(pady=10)
        Label(booking,text="Check Your Booking",font="Ariel 14 bold ",bg='light green',fg='green',relief="raised").grid(column=1, pady=10)
        Label(booking,text="Enter Your Mobile No:",font="Ariel 12 bold ").grid(row=3,column=0)
        mn=Entry(booking,font="Ariel 12 bold ")
        mn.grid(row=3,column=1)
        def check_tic():
            pho=mn.get()
            con=sqlite3.connect('bbsdb.db')
            cur=con.cursor()    
            cur.execute('select * from pass_booking where phone="{0}"'.format(pho))
            res=cur.fetchall()
            if res==[]:
                messagebox.showinfo("Check Bookings","No bookings Found")
            else:
                ticket=Frame(root,relief="groove",borderwidth=5)
                ticket.grid(row=5,column=0,padx=w//3+125,pady=20)
                total=res[0][5]*res[0][10]
                Label(ticket,text="Passengers: "+res[0][1],font="Ariel 10 bold").grid(row=0,column=0)        
                Label(ticket,text="No of Seats: "+str(res[0][5]),font="Ariel 10 bold").grid(row=1,column=0)
                Label(ticket,text="Age:"+str(res[0][3]),font="Ariel 10 bold").grid(row=2,column=0)
                Label(ticket,text="Booking Ref.:"+str(res[0][0]),font="Ariel 10 bold").grid(row=3,column=0)
                Label(ticket,text="Travel On: "+res[0][6],font="Ariel 10 bold").grid(row=4,column=0)
                Label(ticket,text="Fare per Person: ₹"+str(res[0][10]),font="Ariel 10 bold").grid(row=5,column=0)
                Label(ticket,text="Bus ID: "+res[0][12],font="Ariel 10 bold").grid(row=6,column=0)
                Label(ticket,text="Gender: "+res[0][2],font="Ariel 10 bold").grid(row=0,column=2)
                Label(ticket,text="Phone: "+res[0][4],font="Ariel 10 bold").grid(row=1,column=2)
                Label(ticket,text="Total Fare: ₹"+str(total),font="Ariel 10 bold").grid(row=2,column=2)
                Label(ticket,text="Bus Detail: "+str(res[0][9]),font="Ariel 10 bold").grid(row=3,column=2)
                Label(ticket,text="Booked On: "+res[0][7],font="Ariel 10 bold").grid(row=4,column=2)
                Label(ticket,text="Boarding Point: "+res[0][8],font="Ariel 10 bold").grid(row=5,column=2)
                Label(ticket,text="Destination Point: "+res[0][11],font="Ariel 10 bold").grid(row=6,column=2)
                Label(ticket,text="*Total amount ₹"+str(total)+"/- is  to be paid at the time of boarding bus",font="Ariel 8").grid(column=0,columnspan=2)
        def home():
            root.destroy()
            from bbs_gui2 import home
            hm=home()
        Button(booking,image=img2,bd=3,command=home).grid(row=3,column=4,padx=10)
        Button(booking,text="Check Booking",command=check_tic,font="Ariel 12 bold ").grid(row=3,column=2,padx=10)
        root.mainloop()
    
