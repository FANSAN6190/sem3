from tkinter import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
#img=PhotoImage(file="C:\\Users\\211B116\\Desktop\\fansan\\AP\\Lab10\\Project\\Bus_for_project.png")
img=PhotoImage(file="AP/Lab10/project_resources/Bus_for_project.png")

top_frame=Frame(root)
top_frame.grid(row=0,column=0,columnspan=20,padx=w//3)

mid_frame=Frame(root)
mid_frame.grid(row=2,column=0,columnspan=20,padx=w//3,pady=20)


Label(top_frame,image=img).grid(pady=10)
Label(top_frame,text="Online Bus Booking System",font="Ariel 18 bold ", fg='red').grid(pady=20)

def new_operator():
    root.destroy()
    import bbs_gui7
def new_bus():
    root.destroy()
    import bbs_gui8
def new_route():
    root.destroy()
    import bbs_gui9
def new_run():
    root.destroy()
    import bbs_gui10
def mid_frame_content():
    Label(mid_frame,text="Add New Details to Database",font="Ariel 14 bold ",fg='green',relief="solid").grid(columnspan=20,pady=20)
    Button(mid_frame,text="New Operator",command=new_operator, font="Ariel 12 bold ",bg='lime green',activebackground="lime green").grid(row=2,column=1,padx=30)
    Button(mid_frame,text="New Bus",command=new_bus,font="Ariel 12 bold ",bg='tomato',activebackground="tomato").grid(row=2,column=2,padx=30)
    Button(mid_frame,text="New Route",command=new_route,font="Ariel 12 bold ",bg='RoyalBlue1',activebackground="RoyalBlue1").grid(row=2,column=3,padx=30)
    Button(mid_frame,text="New Run",command=new_run,font="Ariel 12 bold ",bg='LightPink3',activebackground="LightPink3").grid(row=2,column=4,padx=30)
mid_frame_content()
root.mainloop()