from tkinter import*
window=Tk()
window.title("employee salary cal")
window.configure(bg="orange")
window.geometry("600x600")


labeltitle=Label(window,text="Employee Salary cal",bg="orange",fg="gray",font=("arial bold italic",20,))
labeltitle.place(x=150,y=0)

labelname=Label(window,text="Enter employee name",bg="orange",font=(10,))
labelname.place(x=0,y=70)


labelname1=Label(window,text="Enter employee number",bg="orange",font=(10,))
labelname1.place(x=0,y=120)

labelhour=Label(window,text="Enter employee work hours",bg="orange",font=(10,))
labelhour.place(x=0,y=180)


labelrup=Label(window,text="Enter 1 hour rupees",bg="orange",font=(10))
labelrup.place(x=0,y=240)

labels=Label(window,bg="orange",font=("arial bold italic",15),fg="red")
labels.place(x=90,y=520)

labelemployee=Label(window,bg="orange",font=("arial bold italic",15))
labelemployee.place(x=90,y=420)

labelnumber=Label(window,bg="orange",font=("arial bold italic",15))
labelnumber.place(x=90,y=470)


data1=Entry(window,width=30)
data1.place(x=200,y=70)

data2=Entry(window,width=10)
data2.place(x=200,y=120)



data3=Entry(window,width=10)
data3.place(x=200,y=180)

data4=Entry(window,width=10)
data4.place(x=150,y=245)




def cal():
    try:

        name=data1.get()
        number=int(data2.get())
        no1=int(data3.get())
        no2=float(data4.get())
        x=(no1*no2)
        labelemployee.config(text= "Employee name : " +name)
        labelnumber.config(text= "Employee number : "+str(number))

        if x >=1000:
           finalsalary=(x+500)
           labels.config(text="Your extra bonus = Rs 500""\n""Final salary = Rs "+str(finalsalary))


        else:
           if x>=500:
             finalsalary=(x+400)
             labels.config(text="Your extra bonus = Rs 400""\n""Final salary = Rs "+str(finalsalary))
           else:
              if x>=300:
                 finalsalary=(x+100)
                 labels.config(text="Your extra bonus = Rs 100""\n""Final salary = Rs "+str(finalsalary))
              else:
                 if x<300:
                     labels.config(text="Final salary = "+str(x))



    except:
        labels.config(text="invalid")



def clear():
    data1.delete(0)
    data2.delete(0)
    data3.delete(0)
    data4.delete(0)
    name=""
    number=""
    value=""
    labelemployee.config(text=name)
    labelnumber.config(text=name)
    labels.config(text=value)










button=Button(window,text="Calculate",bg="red",width=7,font=("arial bold",10),pady=10,command=cal)
button.place(x=30,y=330)


buttonclear=Button(window,text="Clear",bg="green",width=7,font=("arial bold",10),pady=10,command=clear)
buttonclear.place(x=150,y=330)






window.mainloop()

