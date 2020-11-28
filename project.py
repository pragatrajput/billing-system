from tkinter import*
import random
import time;

root=Tk()
root.geometry("1600x1000+0+0")
root.title("---Kalyani Agro Agency---")

text_Input =StringVar()
operator =""

Tops=Frame(root,width=1600,height=50,bg="light blue",relief=SUNKEN)
Tops.pack(side=TOP)

f2=Frame(root,width=800,height=30,relief=SUNKEN)
f2.pack(side=TOP)

f1=Frame(root,width=1600,height=30,bg="khaki1",relief=SUNKEN)
f1.pack(side=TOP)

f3=Frame(root,width=1600,height=30,relief=SUNKEN)
f3.pack(side=TOP)

f4=Frame(root,width=1600,height=50,relief=SUNKEN)
f4.pack(side=TOP)

f41=Frame(root,width=1600,height=30,relief=SUNKEN)
f41.pack(side=TOP)

f7=Frame(root,width=1600,height=40,relief=SUNKEN)
f7.pack(side=TOP)

f5=Frame(root,width=1600,height=30,relief=SUNKEN)
f5.pack(side=TOP)

f6=Frame(root,width=1600,height=12,relief=SUNKEN)
f6.pack(side=TOP)

#=======================================================================================================================
localtime=time.asctime(time.localtime(time.time()))
#=================================================TOP==================================================================
lblInfo = Label(Tops, font=('arial',10, 'bold'),text="pro1prietor-Eknath Rajput(Bsc.(agri))",fg="black",bd=10, anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo = Label(Tops, font=('arial',20, 'bold'),text="--KALYANI  AGRO  AGENCY--",fg="green",bd=12, anchor='w')
lblInfo.grid(row=0,column=1)

lblInfo = Label(Tops, font=('arial',10, 'bold'),text=localtime,fg="black",bd=5, anchor='w')
lblInfo.grid(row=0,column=2)
#-------------------------------------------------F1--------------------------------------------------------------------
rand = StringVar()
ref = StringVar()
Add = StringVar()
Mob = StringVar()
Cash= StringVar()
Remain=IntVar()

lblName =Label(f1,font=('arial',13,'bold'),text="Customer Name:-",bd=12,anchor='w')
lblName.grid(row=0,column=0)

txtName=Entry(f1,font=('arial',13,'bold'), textvariable=rand, bd=10,insertwidth=5 ,bg="pale green",justify='left')
txtName.grid(row=0,column=1)

lblAdd =Label(f1,font=('arial',11,'bold'),text="Address:-",bd=12,anchor='w')
lblAdd.grid(row=0,column=2)
txtAdd=Entry(f1,font=('arial',11,'bold'), textvariable=Add, bd=10,insertwidth=5,bg="pale green",justify='left')
txtAdd.grid(row=0,column=3)

lblMob =Label(f1,font=('arial',9,'bold'),text="Mobile_No:-",bd=12,anchor='w')
lblMob.grid(row=0,column=4)
txtMob=Entry(f1,font=('arial',9,'bold'), textvariable=Mob, bd=10,insertwidth=5,bg="pale green",justify='left')
txtMob.grid(row=0,column=5)
lblMob =Label(f1,font=('arial',9,'bold'),text="Reference",bd=12,anchor='w')
lblMob.grid(row=0,column=6)
txtMob=Entry(f1,font=('arial',9,'bold'), textvariable=ref, bd=10,insertwidth=5,bg="pale green",justify='left')
txtMob.grid(row=0,column=7)
#-------------------------------------------------F2--------------------------------------------------------------------
lblInfo = Label(f2, font=('arial',8, 'bold'),text="=====================================================================",fg="red",anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(f2, font=('arial',10, 'bold'),text="Enter Detail",fg="blue",bd=12, anchor='w')
lblInfo.grid(row=0,column=1)
lblInfo = Label(f2, font=('arial',8, 'bold'),text="=====================================================================",fg="red",anchor='w')
lblInfo.grid(row=0,column=2)
#-------------------------------------------------F3----------------------------------------------------------------------
lblInfo = Label(f3, font=('arial',8, 'bold'),text="=====================================================================",fg="red",anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(f3, font=('arial',10, 'bold'),text="pro1duct Detail",fg="blue",bd=12, anchor='w')
lblInfo.grid(row=0,column=1)
lblInfo = Label(f3, font=('arial',8, 'bold'),text="=====================================================================",fg="red",anchor='w')
lblInfo.grid(row=0,column=2)
#------------------------------------------------F41----------------------------------------------------------------------
lblInfo = Label(f41, font=('arial',8, 'bold'),text="=======================================================",fg="red",anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(f41, font=('arial',10, 'bold'),text="fertilizer detail (Note:-servent charge applicable 3 Rs./bag)",fg="blue",bd=12, anchor='w')
lblInfo.grid(row=0,column=1)
lblInfo = Label(f41, font=('arial',8, 'bold'),text="========================================================",fg="red",anchor='w')
lblInfo.grid(row=0,column=2)
#-----------------------------------------------------f4-----------------------------------------------------------------
Cotton=IntVar()
Bat1=IntVar()
CMRP1=IntVar()
Exp1=StringVar()
pro1=StringVar()

Corn=IntVar()
Bat2=IntVar()
CMRP2=IntVar()
Exp2=StringVar()
pro2=StringVar()

wheat=IntVar()
Bat20=IntVar()
CMRP20=IntVar()
Exp20=StringVar()
pro20=StringVar()

Urea=IntVar()
Bat3=IntVar()
CMRP3=IntVar()
Exp3=StringVar()
pro3=StringVar()

An=IntVar()
Bat4=IntVar()
CMRP4=IntVar()
Exp4=StringVar()
pro4=StringVar()

Dap=IntVar()
Bat5=IntVar()
CMRP5=IntVar()
Exp5=StringVar()
pro5=StringVar()

Oth=IntVar()
pro6=StringVar()
Bat6=IntVar()
CMRP6=IntVar()
Exp6=StringVar()

Sub=IntVar()
Servent=IntVar()
CGst=IntVar()
SGst=IntVar()
Total=StringVar()

Mail=StringVar()
Sr=StringVar()
com1=StringVar()
com2=StringVar()
com3=StringVar()
com4=StringVar()
com6=StringVar()
com5=StringVar()
com20=StringVar()
'''lblSr =Label(f4,font=('arial',10,'bold'),text="Sr.No-",bd=16,anchor='w')
lblSr.grid(row=0,column=0)
txtSr=Entry(f4,font=('arial',10,'bold'), textvariable=Sr, bd=10,insertwidth=5,bg="pale green",justify='left')
txtSr.grid(row=1,column=0)
'''
lblpro1 =Label(f4,font=('arial',10,'bold'),text="Product Name:-",bd=16,anchor='w')
lblpro1.grid(row=0,column=0)
txtpro1=Entry(f4,font=('arial',10,'bold'), textvariable=pro1, bd=10,insertwidth=5,bg="pale green",justify='left')
txtpro1.grid(row=1,column=0)

lblcom =Label(f4,font=('arial',10,'bold'),text="Mass",bd=16,anchor='w')
lblcom.grid(row=0,column=1)
txtcom=Entry(f4,font=('arial',10,'bold'), textvariable=com1, bd=10,insertwidth=5,bg="pale green",justify='left')
txtcom.grid(row=1,column=1)

lblBat1 =Label(f4,font=('arial',10,'bold'),text="Batch_No",bd=16,anchor='w')
lblBat1.grid(row=0,column=2)
txtBat1 =Entry(f4,font=('arial',10,'bold'), textvariable=Bat1, bd=10,insertwidth=5,bg="pale green",justify='left')
txtBat1.grid(row=1,column=2)

lblExp1 =Label(f4,font=('arial',10,'bold'),text="Exp_Date",bd=16,anchor='w')
lblExp1.grid(row=0,column=3)
txtExp1 =Entry(f4,font=('arial',10,'bold'), textvariable=Exp1, bd=10,insertwidth=5,bg="pale green",justify='left')
txtExp1.grid(row=1,column=3)

lblCotton =Label(f4,font=('arial',10,'bold'),text="Quantity",bd=16,anchor='w')
lblCotton.grid(row=0,column=4)
txtCotton=Entry(f4,font=('arial',10,'bold'), textvariable=Cotton, bd=10,insertwidth=5,bg="pale green",justify='left')
txtCotton.grid(row=1,column=4)

lblCMRP1 =Label(f4,font=('arial',10,'bold'),text="MRP",bd=16,anchor='w')
lblCMRP1.grid(row=0,column=5)
txtCMRP1 =Entry(f4,font=('arial',10,'bold'), textvariable=CMRP1, bd=10,insertwidth=5,bg="pale green",justify='left')
txtCMRP1.grid(row=1,column=5)

#---------------------------------------------------------------------------------------------------------------------------

txtpro1=Entry(f4,font=('arial',10,'bold'), textvariable=pro2, bd=10,insertwidth=5,bg="pale green",justify='left')
txtpro1.grid(row=2,column=0)

txtcom=Entry(f4,font=('arial',10,'bold'), textvariable=com2, bd=10,insertwidth=5,bg="pale green",justify='left')
txtcom.grid(row=2,column=1)

txtBat2=Entry(f4,font=('arial',10,'bold'), textvariable=Bat2, bd=10,insertwidth=5,bg="pale green",justify='left')
txtBat2.grid(row=2,column=2)

txtExp2=Entry(f4,font=('arial',10,'bold'), textvariable=Exp2, bd=10,insertwidth=5,bg="pale green",justify='left')
txtExp2.grid(row=2,column=3)

txtCorn=Entry(f4,font=('arial',10,'bold'), textvariable=Corn, bd=10,insertwidth=5,bg="pale green",justify='left')
txtCorn.grid(row=2,column=4)

txtCMRP2=Entry(f4,font=('arial',10,'bold'), textvariable=CMRP2, bd=10,insertwidth=5,bg="pale green",justify='left')
txtCMRP2.grid(row=2,column=5)
#---------------------------------------------------------------------------------------------------------------------------

txtpro1=Entry(f4,font=('arial',10,'bold'), textvariable=pro20, bd=10,insertwidth=5,bg="pale green",justify='left')
txtpro1.grid(row=3,column=0)

txtcom=Entry(f4,font=('arial',10,'bold'), textvariable=com20, bd=10,insertwidth=5,bg="pale green",justify='left')
txtcom.grid(row=3,column=1)

txtBat2=Entry(f4,font=('arial',10,'bold'), textvariable=Bat20, bd=10,insertwidth=5,bg="pale green",justify='left')
txtBat2.grid(row=3,column=2)

txtExp2=Entry(f4,font=('arial',10,'bold'), textvariable=Exp20, bd=10,insertwidth=5,bg="pale green",justify='left')
txtExp2.grid(row=3,column=3)

txtCorn=Entry(f4,font=('arial',10,'bold'), textvariable=wheat, bd=10,insertwidth=5,bg="pale green",justify='left')
txtCorn.grid(row=3,column=4)

txtCMRP2=Entry(f4,font=('arial',10,'bold'), textvariable=CMRP20, bd=10,insertwidth=5,bg="pale green",justify='left')
txtCMRP2.grid(row=3,column=5)
#--------------------------------------------------------------------------------------------------------------------------------------------
'''txtpro6=Entry(f4,font=('arial',10,'bold'), textvariable=pro6, bd=10,insertwidth=5,bg="pale green",justify='left')
txtpro6.grid(row=4,column=0)

txtcom6=Entry(f4,font=('arial',10,'bold'), textvariable=com6, bd=10,insertwidth=5,bg="pale green",justify='left')
txtcom6.grid(row=4,column=1)

txtBat6=Entry(f4,font=('arial',10,'bold'), textvariable=Bat6, bd=10,insertwidth=5,bg="pale green",justify='left')
txtBat6.grid(row=4,column=2)

txtExp6=Entry(f4,font=('arial',10,'bold'), textvariable=Exp6, bd=10,insertwidth=5,bg="pale green",justify='left')
txtExp6.grid(row=4,column=3)

txtOth=Entry(f4,font=('arial',10,'bold'), textvariable=Oth, bd=10,insertwidth=5,bg="pale green",justify='left')
txtOth.grid(row=4,column=4)

txtCMRP6=Entry(f4,font=('arial',10,'bold'), textvariable=CMRP6, bd=10,insertwidth=5,bg="pale green",justify='left')
txtCMRP6.grid(row=4,column=5)
'''#--------------------------------------------------------------------------------------------------------------------------------------------
lblpro1 =Label(f7,font=('arial',10,'bold'),text="Product Name:-",bd=16,anchor='w')
lblpro1.grid(row=0,column=0)
txtpro1=Entry(f7,font=('arial',10,'bold'), textvariable=pro3, bd=10,insertwidth=5,bg="pale green",justify='left')
txtpro1.grid(row=1,column=0)

lblcom =Label(f7,font=('arial',10,'bold'),text="Mass",bd=16,anchor='w')
lblcom.grid(row=0,column=1)
txtcom=Entry(f7,font=('arial',10,'bold'), textvariable=com3, bd=10,insertwidth=5,bg="pale green",justify='left')
txtcom.grid(row=1,column=1)

lblBat3 =Label(f7,font=('arial',10,'bold'),text="Batch_No",bd=16,anchor='w')
lblBat3.grid(row=0,column=2)
txtBat3=Entry(f7,font=('arial',10,'bold'), textvariable=Bat3, bd=10,insertwidth=5,bg="pale green",justify='left')
txtBat3.grid(row=1,column=2)

lblExp3 =Label(f7,font=('arial',10,'bold'),text="Exp_Date",bd=16,anchor='w')
lblExp3.grid(row=0,column=3)
txtExp3=Entry(f7,font=('arial',10,'bold'), textvariable=Exp3, bd=10,insertwidth=5,bg="pale green",justify='left')
txtExp3.grid(row=1,column=3)

lblBat3 =Label(f7,font=('arial',10,'bold'),text="quantity",bd=16,anchor='w')
lblBat3.grid(row=0,column=4)
txtUrea=Entry(f7,font=('arial',10,'bold'), textvariable=Urea, bd=10,insertwidth=5,bg="pale green",justify='left')
txtUrea.grid(row=1,column=4)

lblCMRP3=Label(f7,font=('arial',10,'bold'),text="MRP",bd=16,anchor='w')
lblCMRP3.grid(row=0,column=5)
txtCMRP3=Entry(f7,font=('arial',10,'bold'), textvariable=CMRP3, bd=10,insertwidth=5,bg="pale green",justify='left')
txtCMRP3.grid(row=1,column=5)
#---------------------------------------------------------------------------------------------------------------------------

txtpro1=Entry(f7,font=('arial',10,'bold'), textvariable=pro4, bd=10,insertwidth=5,bg="pale green",justify='left')
txtpro1.grid(row=2,column=0)

txtcom=Entry(f7,font=('arial',10,'bold'), textvariable=com4, bd=10,insertwidth=5,bg="pale green",justify='left')
txtcom.grid(row=2,column=1)

txtBat4=Entry(f7,font=('arial',10,'bold'), textvariable=Bat4, bd=10,insertwidth=5,bg="pale green",justify='left')
txtBat4.grid(row=2,column=2)

txtExp4=Entry(f7,font=('arial',10,'bold'), textvariable=Exp4, bd=10,insertwidth=5,bg="pale green",justify='left')
txtExp4.grid(row=2,column=3)

txtAn=Entry(f7,font=('arial',10,'bold'), textvariable=An, bd=10,insertwidth=5,bg="pale green",justify='left')
txtAn.grid(row=2,column=4)

txtCMRP4=Entry(f7,font=('arial',10,'bold'), textvariable=CMRP4, bd=10,insertwidth=5,bg="pale green",justify='left')
txtCMRP4.grid(row=2,column=5)
#---------------------------------------------------------------------------------------------------------------------------

txtpro1=Entry(f7,font=('arial',10,'bold'), textvariable=pro5, bd=10,insertwidth=5,bg="pale green",justify='left')
txtpro1.grid(row=3,column=0)

txtcom=Entry(f7,font=('arial',10,'bold'), textvariable=com5, bd=10,insertwidth=5,bg="pale green",justify='left')
txtcom.grid(row=3,column=1)

txtBat5=Entry(f7,font=('arial',10,'bold'), textvariable=Bat5, bd=10,insertwidth=5,bg="pale green",justify='left')
txtBat5.grid(row=3,column=2)

txtExp5=Entry(f7,font=('arial',10,'bold'), textvariable=Exp5, bd=10,insertwidth=5,bg="pale green",justify='left')
txtExp5.grid(row=3,column=3)

txtDap=Entry(f7,font=('arial',10,'bold'), textvariable=Dap, bd=10,insertwidth=5,bg="pale green",justify='left')
txtDap.grid(row=3,column=4)

txtCMRP5=Entry(f7,font=('arial',10,'bold'), textvariable=CMRP5, bd=10,insertwidth=5,bg="pale green",justify='left')
txtCMRP5.grid(row=3,column=5)
#---------------------------------------------------------------------------------------------------------------------------


lblRemaining =Label(f7,font=('arial',10,'bold'),text="Deposit",bd=16,anchor='w')
lblRemaining.grid(row=0,column=6)
txtRemaining=Entry(f7,font=('arial',10,'bold'), textvariable=Remain, bd=10,insertwidth=5,bg="plum1",justify='left')
txtRemaining.grid(row=1,column=6)

lblCash =Label(f7,font=('arial',10,'bold'),text="Cash_Type:-",bd=16,anchor='w')
lblCash.grid(row=2,column=6)
txtCash=Entry(f7,font=('arial',10,'bold'), textvariable=Cash, bd=10,insertwidth=5,bg="plum1",justify='left')
txtCash.grid(row=3,column=6)
'''
lblMail =Label(f4,font=('arial',10,'bold'),text="Mail_Id",bd=16,anchor='w')
lblMail.grid(row=4,column=4)
txtMail=Entry(f4,font=('arial',10,'bold'), textvariable=Mail, bd=10,insertwidth=5,bg="plum1",justify='left')
txtMail.grid(row=4,column=5)
'''

#--------------------------------------------------------------------------------------------------------------------
def Tot():
    x=random.randint(0,500876)
    randomRef = str(x)
    ref.set(randomRef)
    
    CoSeed = float(Cotton.get())
    CoSCORN = float(Corn.get())
    CoU = float(Urea.get())
    CoAn = float(An.get())
    CoDap = float(Dap.get())
    CoOth = float(Oth.get())
    Cowheat= float(wheat.get())
    CoRemain=float(Remain.get())

    CoMrp1=float(CMRP1.get())
    CoMrp2=float(CMRP2.get())
    CoMrp20=float(CMRP20.get())
    CoMrp3=float(CMRP3.get())
    CoMrp4=float(CMRP4.get())
    CoMrp5=float(CMRP5.get())
    CoMrp6=float(CMRP6.get())

    CostOfCotton=CoSeed * CoMrp1
    CostOfCorn=CoSCORN * CoMrp2
    CostOfWheat= Cowheat * CoMrp20
    CostOfUrea=CoU * CoMrp3
    CostOfAn=CoAn * CoMrp4
    CostOfDap=CoDap * CoMrp5
    CostOfOth=CoOth * CoMrp6

    CostOfItems="Rs",str('%.2f'%(CostOfCotton +  CostOfCorn + CostOfUrea + CostOfAn + CostOfDap + CostOfOth +  Cowheat ))
    Ser_Charge=  ((CoU + CoAn + CoDap)*3)
    CGST=((CostOfCotton +  CostOfCorn + CostOfUrea + CostOfAn + CostOfDap + CostOfOth +  Cowheat ) * 0.09)
    SGST=((CostOfCotton +  CostOfCorn + CostOfUrea + CostOfAn + CostOfDap + CostOfOth +  Cowheat ) * 0.09)

    TotalCost =  (CostOfCotton +  CostOfCorn + CostOfUrea + CostOfAn + CostOfDap + CostOfOth +  Cowheat - CoRemain)
    
    OverAllCost= "Rs",str('%.2f'%(TotalCost + CGST + SGST))
    Service= "Rs",str('%.2f'%Ser_Charge)
    PaidCGst="Rs",str('%.2f'%CGST)
    PaidSGst="Rs",str('%.2f'%SGST)
    Servent.set(Service)
    Sub.set(CostOfItems)
    CGst.set(PaidCGst)
    SGst.set(PaidSGst)
    Total.set(OverAllCost)
    #btnTotal=Button(f4,padx=16,pady=4,bd=15,fg="Black",font=('arial',12,'bold'), width=8,text="Thank You",bg="red",command=Tot).grid(row=3,column=3)
    

btnTotal=Button(f6,padx=16,pady=4,bd=15,fg="Black",font=('arial',12,'bold'), width=8,text="Total",bg="gold",command=Tot).grid(row=1,column=3)

def save():
    text ="\n"+localtime+"\n "+"1}Customer_Name:-"+rand.get() +" "+"2}Address:-"+Add.get()+" "+"3}Mobile No>"+Mob.get()+" "+"4}Total:-"+Total.get()

    with open("text.txt", "a") as f:
        f.write(text)
btnSave=Button(f6,padx=16,pady=4,bd=15,fg="Black",font=('arial',12,'bold'), width=8,text="Save",bg="gold",command=save).grid(row=1,column=4)


#---------------------------------------------F5-----------------------------------------------------------------------
lblInfo = Label(f5, font=('arial',8, 'bold'),text="=======================================================================================",fg="red",anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(f5, font=('arial',10, 'bold'),text="Payment Detail",fg="blue",bd=12, anchor='w')
lblInfo.grid(row=0,column=1)
lblInfo = Label(f5, font=('arial',8, 'bold'),text="=======================================================================================",fg="red",anchor='w')
lblInfo.grid(row=0,column=2)
#---------------------------------------------F6------------------------------------------------------------------------

lblSub =Label(f6,font=('arial',12,'bold'),text="Sub_Total",bd=15,anchor='w')
lblSub.grid(row=0,column=0)
txtSub=Entry(f6,font=('arial',12,'bold'), textvariable=Sub, bd=10,insertwidth=5,bg="coral1",justify='left')
txtSub.grid(row=0,column=1)

lblServent =Label(f6,font=('arial',12,'bold'),text="Servent_Charge",bd=15,anchor='w')
lblServent.grid(row=0,column=2)
txtServent=Entry(f6,font=('arial',12,'bold'), textvariable=Servent, bd=10,insertwidth=5,bg="coral1",justify='left')
txtServent.grid(row=0,column=3)

lblCGst =Label(f6,font=('arial',12,'bold'),text="CGST",bd=15,anchor='w')
lblCGst.grid(row=0,column=4)
txtCGst=Entry(f6,font=('arial',12,'bold'), textvariable=CGst, bd=10,insertwidth=5,bg="coral1",justify='left')
txtCGst.grid(row=0,column=5)

lblSGst =Label(f6,font=('arial',12,'bold'),text="SGST",bd=15,anchor='w')
lblSGst.grid(row=0,column=6)
txtSGst=Entry(f6,font=('arial',12,'bold'), textvariable=SGst, bd=10,insertwidth=5,bg="coral1",justify='left')
txtSGst.grid(row=0,column=7)
#------------------------------------------F7-----------------------------------------------------------------------------

lblTotal =Label(f6,font=('arial',15,'bold'),text="Total",bd=15,anchor='w')
lblTotal.grid(row=1,column=6)
txtTotal=Entry(f6,font=('arial',13,'bold'), textvariable=Total, bd=10,insertwidth=5,bg="red",justify='left')
txtTotal.grid(row=1,column=7)

#=------------------------------------------------------------------------------------------------------------------------
def qExit():
   root.destroy()
btnExit=Button(f6,padx=16,pady=4,bd=15,fg="Black",font=('arial',12,'bold'), width=8,text="Exit",bg="red",command=qExit).grid(row=1,column=0)

def Reset():
    rand.set("")
    Add.set("")
    Mob.set("")
    Cash.set("")
    Remain.set("")
    #pro1.set(0)
    Cotton.set(0)
    Corn.set(0)
    Urea.set(0)
    An.set(0)
    Dap.set(0)
    Oth.set(0)
    Mail.set("")

    Exp1.set("")
    Exp2.set("")
    Exp3.set("")
    Exp4.set("")
    Exp5.set("")
    Exp6.set("")
    
    CMRP1.set(0)
    CMRP2.set(0)
    CMRP3.set(0)
    CMRP4.set(0)
    CMRP5.set(0)
    CMRP6.set(0)
    
    Bat1.set(0)
    Bat2.set(0)
    Bat3.set(0)
    Bat4.set(0)
    Bat5.set(0)
    Bat6.set(0)

    pro1.set("")
    pro2.set("")
    pro3.set("")
    pro4.set("")
    pro5.set("")
    pro6.set("")

    com1.set("")
    com2.set("")
    com3.set("")
    com4.set("")
    com5.set("")
    com6.set("")
    
    
    Sub.set(0)
    Servent.set(0)
    CGst.set(0)
    SGst.set(0)
    Total.set("")
    

btnReset=Button(f6,padx=16,pady=4,bd=15,fg="Black",font=('arial',12,'bold'), width=8,text="Paid",bg="gold",command=Reset).grid(row=1,column=1)

btnPrint=Button(f6,padx=16,pady=4,bd=15,fg="Black",font=('arial',12,'bold'), width=8,text="Print",bg="gold").grid(row=1,column=2)
#btnSend=Button(f6,padx=16,pady=4,bd=15,fg="Black",font=('arial',12,'bold'), width=8,text="SEND",bg="light coral").grid(row=1,column=1)




root.mainloop()







