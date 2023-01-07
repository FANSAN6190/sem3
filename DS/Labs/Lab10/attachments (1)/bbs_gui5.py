from tkinter import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
#img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\Bus_for_project.png")
img=PhotoImage(file="AP/Lab10/project_resources/Bus_for_project.png")
top_frame=Frame(root)
top_frame.grid(row=0,column=0,padx=w//3+125)

booking=Frame(root,relief="solid",borderwidth=2)
booking.grid(row=2,column=0,padx=w//3+125,pady=20)

Label(top_frame,image=img).grid(pady=10)
Label(top_frame,text="Online Bus Booking System",font="Ariel 18 bold ",bg='light blue',fg='red',relief="raised").grid(pady=10)
Label(top_frame,text="Check Your Booking",font="Ariel 14 bold ",bg='light green',fg='green',relief="raised").grid(pady=10)

Label(top_frame,text="Enter Your Mobile No:",font="Ariel 12 bold ").grid(row=3,column=0)
mn=Entry(top_frame,font="Ariel 12 bold ")
mn.grid(row=3,column=1)
Button(top_frame,text="Check Booking",font="Ariel 12 bold ").grid(row=3,column=2,padx=10)

root.mainloop()