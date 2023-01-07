#home
from tkinter import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
#img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\Bus_for_project.png")
img=PhotoImage(file="project_resources/Bus_for_project.png")

def seat_booking():
    root.destroy()
    import bbs_gui3
def check_booking_status():
    root.destroy()
    import bbs_gui5
def add_bus_details():
    root.destroy()
    import bbs_gui6
#----------Main--------------------]
top_frame=Frame(root)
top_frame.grid(row=0,column=2,padx=w//3-40)

mid_frame=Frame(root)
mid_frame.grid(row=2,column=2,padx=w//3-40,pady=20)

Label(top_frame,image=img).grid(pady=10)
Label(top_frame,text="Online Bus Booking System",font="Ariel 18 bold ",bg='light blue',fg='red',relief="groove",bd=2).grid(pady=20)

Button(mid_frame,text="Seat Booking",command=seat_booking,font="Ariel 12 bold ",bg="#91e288",activebackground="#91e288").grid(row=2,column=1,padx=30)
Button(mid_frame,text="Check Booked Seats",command=check_booking_status,font="Ariel 12 bold ",bg='green3',activebackground="green3").grid(row=2,column=2,padx=30)
Button(mid_frame,text="Add Bus Details",command=add_bus_details,font="Ariel 12 bold ",bg='green4',activebackground="green4").grid(row=2,column=3,padx=30)
Label(mid_frame,text="For Admins Only",font="Ariel 10 bold ",fg='red').grid(row=4,column=3,padx=30,pady=10)
#-----------------------------------
root.mainloop()

