from tkinter import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
#img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\Bus_for_project.png")
img=PhotoImage(file="AP/Lab10/project_resources/Bus_for_project.png")

top_frame=Frame(root)
top_frame.grid(row=0,column=2,padx=w//3)

mid_frame=Frame(root)
mid_frame.grid(row=2,column=2,padx=w//3,pady=20)


Label(top_frame,image=img).grid(pady=10)
Label(top_frame,text="Online Bus Booking System",font="Ariel 18 bold ",bg='light blue',fg='red').grid(pady=20)

Button(mid_frame,text="Seat Booking",font="Ariel 12 bold ",bg='lime green',activebackground="lime green").grid(row=2,column=1,padx=30)
Button(mid_frame,text="Check Booked Seats",font="Ariel 12 bold ",bg='green3',activebackground="green3").grid(row=2,column=2,padx=30)
Button(mid_frame,text="Add Bus Details",font="Ariel 12 bold ",bg='green4',activebackground="green4").grid(row=2,column=3,padx=30)
Label(mid_frame,text="For Admins Only",font="Ariel 10 bold ",fg='red').grid(row=4,column=3,padx=30,pady=10)
root.mainloop()
