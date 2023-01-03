from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
 
def main():
    root = Tk()
    app = Window1(root)
    root.mainloop()
    return
 
class Window1:
    def __init__(self,master):
        self.master = master
        self.master.title("Test Login System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg ='powder blue')
        self.frame.pack()
 
        self.username = StringVar()
        self.password = StringVar()
        self.lblTitle = Label(self.frame,  text = 'Sealant Login System', font = ('arial',30,'bold'), bg='powder blue',
                              fg = 'black')
        self.lblTitle.grid(row=0, columnspan = 2, pady = 40)
 
        #==================================================================================================
 
        self.LoginFrame1 = LabelFrame(self.frame, width = 1350, height = 600
                                ,font = ('arial',20,'bold'), relief = 'ridge', bg = 'cadet blue', bd = 20)
        self.LoginFrame1.grid(row = 1, column =0)
 
        self.LoginFrame2 = LabelFrame(self.frame, width=1000, height=600
                                ,font=('arial', 20, 'bold'), relief='ridge', bg='cadet blue', bd = 20)
        self.LoginFrame2.grid(row=2, column=0)
 
        #=====================================Label and Entry==============================================
 
        self.lblUsername = Label(self.LoginFrame1,text = 'Username', font=('arial', 10, 'bold'), bd = 22,
                                 bg= 'cadet blue', fg = 'Cornsilk')
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.LoginFrame1, font = ('arial', 15, 'bold'),textvariable= self.username)
        self.txtUsername.grid(row=0, column=1, padx =8, pady =8)
 
        self.lblpassword = Label(self.LoginFrame1,text = 'Password', font=('arial', 10, 'bold'),bd = 22,
                                 bg= 'cadet blue', fg = 'Cornsilk')
        self.lblpassword.grid(row=1, column=0, padx =8, pady =8)
        self.txtpassword = Entry(self.LoginFrame1, font = ('arial', 15, 'bold'), textvariable= self.password)
        self.txtpassword.grid(row=1, column=1)
 
        #=====================================Button========================================================
        self.btnLogin = Button(self.LoginFrame2, text='Login', width=17, font = ('arial', 8), command = self.Login_System)
        self.btnLogin.grid(row=0, column=1, padx =10, pady =10)
 
        self.btnReset = Button(self.LoginFrame2, text='Reset', width=17, font = ('arial', 8), command = self.Rest)
        self.btnReset.grid(row=0, column=2, padx =10, pady =10)
 
        self.btnExit = Button(self.LoginFrame2, text='Exit', width=17, font = ('arial', 8), command = self.iExit)
        self.btnExit.grid(row=0, column=3, padx =10, pady =10)
 
    def Login_System(self):
        u = (self.username.get())
        p = (self.password.get())
 
        if (u == str("admin") and p == str("admin")):
 
            self.newWindow = Toplevel(self.master)
            self.app = Window2(self.newWindow)
 
        else:
            tkinter.messagebox.askyesno("Login System","Invalid Login Detail")
            self.username.set("")
            self.password.set("")
            self.txtUsername.focus()
 
    def Rest(self):
        self.username.set("")
        self.password.set("")
        self.txtUsername.focus()
 
    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Login System", "Are You Sure you want to Exit?")
        if self.iExit > 0:
            self.master.destroy()
        else:
            command = self.new_window
            return
 
 
    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)
 
 
class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Test Reference System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()
 
 
if __name__ == '__main__':
    main()