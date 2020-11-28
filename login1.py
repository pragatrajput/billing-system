from tkinter import *
import tkinter.messagebox as tm
import subprocess

root=Tk()
root.geometry("800x400+0+0")
root.title("Login Detail")

Tops=Frame(root,width=1600,height=60,bg="light blue",relief=SUNKEN)
Tops.pack(side=TOP)

f2=Frame(root,width=1600,height=60,relief=FLAT)
f2.pack(side=TOP)

user=StringVar()
Pass=StringVar()

lblName =Label(Tops,font=('arial',13,'bold'),text="Developed by Pragat Rajput ",bd=12,anchor='w')
lblName.grid(row=0,column=0)
lblName =Label(Tops,font=('arial',13,'bold'),text="Enter username and password ",bd=12,anchor='w')
lblName.grid(row=1,column=0)

lbluser =Label(f2,font=('arial',10,'bold'),text="User Name:-",bd=12,anchor='w')
lbluser.grid(row=0,column=0)
txtuser=Entry(f2,font=('arial',10,'bold'), textvariable=user, bd=10,insertwidth=5 ,bg="white",justify='left')
txtuser.grid(row=0,column=1)

lblName =Label(f2,font=('arial',10,'bold'),text="password:",bd=12,anchor='w')
lblName.grid(row=1,column=0)
txtName=Entry(f2,font=('arial',10,'bold'), textvariable=Pass,show="*", bd=10,insertwidth=5 ,bg="white",justify='left')
txtName.grid(row=1,column=1)

def logi():
    username=user.get()
    Password=Pass.get()
    if username=="Pragat" and Password=="Pragat":
              subprocess.call(['python', 'project.py'])
    else:
            tm.showerror("Login error", "Incorrect username or password")

sbtnLogin=Button(f2,padx=10,pady=4,bd=7,fg="Black",font=('arial',7,'bold'),text="Login",bg="pale green",command=logi).grid(row=2,column=1)
root.mainloop
