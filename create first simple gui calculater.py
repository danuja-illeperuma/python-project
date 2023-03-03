#පයිතන් සරල කැල්කුලේටරය

from tkinter import*
window=Tk()
window.title("Welcome to phython GUI")
window.configure(bg="yellow")
window.geometry("300x300")


label=Label(window,text="simple calculator",font="times 20 bold",bg="yellow")
label.grid(row=0,column=1)

labeln1=Label(window,text="Enter no1 :",bg="yellow")
labeln1.grid(row=1,column=0)

data1=Entry(window,width="30")
data1.grid(row=1,column=1)


labeln2=Label(window,text="Enter no2 :",bg="yellow")
labeln2.grid(row=2,column=0)

data2=Entry(window,width="30")
data2.grid(row=2,column=1)


labeltot=Label(window,bg="yellow")
labeltot.grid(row=3,column=1)

def totbutton():
 try:
    no1=int(data1.get())
    no2=int(data2.get())
    tot=str(no1+no2)
    labeltot.config(text=tot)

 except ValueError:
             labeltot.config(text="inavild value")

def clearbutton():
    data1.delete(0)
    data2.delete(0)
    tot=0
    labeltot.config(text=tot)

buttontot=Button(window,text="Total",bg="orange",command=totbutton)
buttontot.grid(row=4,column=0)

buttonclear=Button(window,text="Clear",bg="red",command=clearbutton)
buttonclear.grid(row=4,column=1)




window.mainloop()

