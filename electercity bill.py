from tkinter import *
window=Tk()
window.title("Electercity bill cal")
window.configure(bg="gray50")
window.geometry("500x500")

labelintro=Label(window,text="Electricity bill calculator",font=("arial bold",25,"underline"),bg="gray50",fg="violetred4")
labelintro.place(x=100,y=0)

label1=Label(window,text="Enter Previous Meter Reading",bg="gray50",font=("arial bold",15))
label1.place(x=0,y=100)

label2=Label(window,text="Enter Current Meter Reading",bg="gray50",font=("arial bold",15))
label2.place(x=0,y=170)

data1=Entry(window,width=10)
data1.place(x=300,y=107)



data2=Entry(window,width=10)
data2.place(x=300,y=175)

bill=Label(window,bg="gray50",font=("arial bold",15))
bill.place(x=150,y=400)

def cal():
 try:
    value=int(data1.get())
    value2=int(data2.get())
    x=(value2-value)

    if x  <= 30:
        total=(x*2.50)+30
        bill.config(text="Total amount : " + str(total))

    elif x <= 60:
        total=(30*2.50)+((x-30)*4.85)+(60)
        bill.config(text="Total amount : " + str(total))
    elif x <= 90:
        total=(60*7.85)+((x-60)*10)+(90)
        bill.config(text="Total amount : " + str(total))

    elif x<=120:
        total=(60*7.85)+(29*10)+((x-89)*27.75)+(480)
        bill.config(text="Total amount : " + str(total))

    elif x<=180:
        total=(60*7.85)+(29*10)+(29*27.75)+((x-118)*32)+(480)
        bill.config(text="Total amount : " + str(total))

    elif x > 180:
        total=(60*7.85)+(29*10)+(29*27.75)+(59*32)+((x-177)*45)+(540)
        bill.config(text="Total amount : " + str(total))

 except:
      bill.config(text="Invalid")


def clearbutton():
    data1.delete(0)
    data2.delete(0)
    total=0
    bill.config(text=total)


















buttoncal=Button(window,text="Calculate",bg="red",font=("arial bold",15),width=7,pady=15,command=cal)
buttoncal.place(x=30,y=250)
buttonclear=Button(window,text="Clear",bg="skyblue",width=5,font=("arial bold",15),pady=15,command=clearbutton)
buttonclear.place(x=200,y=250)

labelowner=Label(window,text="Created by Danuja illeperuma",font=("arial bold",12,"italic"),bg="gray50",fg="darkblue")
labelowner.place(x=250,y=450)


































window.mainloop()