#import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

screen = Tk()
screen.title("Sip Calculator")
a=StringVar()
b=StringVar()
def sip():
    monthly_amount=int(a.get())
    a.set(" ")
    time_period=int(b.get())
    b.set(" ")
    invested_amount=int(monthly_amount*12*time_period)
    tot=int(invested_amount*27.24)
    est_returns=int(tot-invested_amount)
    result_str='Invested_amount:%s \nEst_returns:%s \nTotal_value:%s'%(invested_amount,est_returns,tot)
    result['text']=result_str
    print(monthly_amount)
    print(time_period)
    print(result_str)
img=Image.open(r'profit.jpg')
img=img.resize((900,500),Image.ANTIALIAS)
photos =ImageTk.PhotoImage(img)
Label(screen,image=photos).pack()
screen.geometry("900x500")
#bg_lbl=Label(screen,image=photos)
#bg_lbl.place(x=0,y=0,width=200,height=500)
Title = Label(screen,text="Sip Calculator", font="comicsansms 16 bold",fg='white', bg='blue',width=100)
Title.place(x=-150,y=0)

frame_one=Frame(screen,bg="brown", bd=5)
frame_one.place(x=250,y=60,width=450,height=50)
Label(frame_one,text="Monthly Investment",font="comicsansms 13 bold",bg="brown",fg='white',width=17).place(x=0,y=10)
txt_box1=Entry(frame_one,textvariable=a,font=('times new roman',25), width=15).place(x=180,y=0)
#txt_box.grid(row=80,column=50,sticky='w')


frame_two=Frame(screen,bg="brown", bd=5)
frame_two.place(x=250,y=130,width=450,height=50)
Label(frame_two,text="Time Period (years)",font="comicsansms 13 bold",bg="brown",fg='white',width=17).place(x=0,y=10)
txt_box2=Entry(frame_two,textvariable=b,font=('times new roman',25), width=15).place(x=180,y=0)

#txt_box.grid(row=0,column=0,sticky='w')
frame_three=Frame(screen,bg="dark green", bd=5)
frame_three.place(x=250,y=280,width=450,height=100)
result=Label(frame_three,font=40,bg='white')
result.place(relwidth=1,relheight=1)
Label(screen,text="Expected return rate:12%(p.a)",font="comicsansms 13 bold",fg='red',).place(x=250,y=190)
Button(screen,text='Calculate',font="comicsansms 16 bold", fg='white',bg='blue',command=sip).place(x=450,y=220)

screen.mainloop()