from tkinter import *
from tkinter.messagebox import showinfo
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
#img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\Bus_for_project.png")
img=PhotoImage(file="AP/Lab10/project_resources/Bus_for_project.png")
showinfo("Success","Seat Booked.....")
top_frame=Frame(root)
top_frame.grid(row=0,column=0,padx=w//3+125)

ticket=Frame(root,relief="solid",borderwidth=2)
ticket.grid(row=2,column=0,padx=w//3+125,pady=20)

Label(top_frame,image=img).grid(pady=10)
Label(top_frame,text="Online Bus Booking System",font="Ariel 18 bold ",bg='light blue',fg='red').grid(pady=10)

Label(top_frame,text="Bus Ticket",font="Ariel 10 bold").grid()
Label(ticket,text="Passengers:",font="Ariel 10 bold",justify=LEFT).grid(row=0,column=0)
Label(ticket,text="No of Seats:",font="Ariel 10 bold").grid(row=1,column=0)
Label(ticket,text="Age:",font="Ariel 10 bold").grid(row=2,column=0)
Label(ticket,text="Booking Ref.:",font="Ariel 10 bold").grid(row=3,column=0)
Label(ticket,text="Travel On",font="Ariel 10 bold").grid(row=4,column=0)
Label(ticket,text="No of Seats:",font="Ariel 10 bold").grid(row=5,column=0)
Label(ticket,text="Gender:",font="Ariel 10 bold").grid(row=0,column=1)
Label(ticket,text="Phone:",font="Ariel 10 bold").grid(row=1,column=1)
Label(ticket,text="Fare Rs:",font="Ariel 10 bold").grid(row=2,column=1)
Label(ticket,text="Bus Detail:",font="Ariel 10 bold").grid(row=3,column=1)
Label(ticket,text="Booked On:",font="Ariel 10 bold").grid(row=4,column=1)
Label(ticket,text="Boarding Point:",font="Ariel 10 bold").grid(row=5,column=1)
Label(ticket,text="*Total amount Rs."+"/- to be paid at the time of boarding bus",font="Ariel 8").grid()
root.mainloop()