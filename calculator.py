from tkinter import *


def btnclick(number):
    global operator
    operator= operator + str(number)
    text_Input.set(operator)

def btnclc():
    global operator
    operator="0"
    text_Input.set(operator)
    operator=""

def btneq():
    global operator
    res = eval(operator)
    if(isinstance(res, float)):
         text_Input.set("{0:.5f}".format(res))
         operator=""
         return
    text_Input.set(res)
    operator=""

def back():
    global operator
    operator = text_Input.get()[:-1]
    if operator == "":
          operator = "0"
          text_Input.set(operator)
          operator=""
          return
    text_Input.set(operator)
    
    


cal = Tk()
cal.title("Calculator")
cal.geometry("345x400")
operator = ""
text_Input = StringVar()

txtdisplay = Entry(cal,font=('arial',19),textvariable=text_Input,bd=30,insertwidth=4,bg="#61faf2",justify='right').grid(columnspan=4)


clear = Button(cal,padx=16,bd=8, fg="black" ,bg="#e64215",font=('arial',17),text="AC",command=btnclc).place(x=5,y=95)
bac = Button(cal,padx=16,bd=8, fg="black" ,bg="#e64215",font=('arial',17),text="Backspace",command=back).place(x=97,y=95)
#mod = Button(cal,padx=16,bd=8, fg="black" ,font=('arial',20),text="%").grid(row=1,column=2)
div= Button(cal,padx=18,bd=8, fg="black" ,bg="#56a4d1",font=('arial',17),text="/",command=lambda:btnclick("/")).place(x=273,y=95)


btn7 = Button(cal,padx=24,bd=8, fg="white" ,bg="#919c9a",font=('arial',17),text="7",command=lambda:btnclick(7)).place(x=5,y=155)
btn8 = Button(cal,padx=22,bd=8, fg="white" ,bg="#919c9a",font=('arial',17),text="8",command=lambda:btnclick(8)).place(x=97,y=155)
btn9 = Button(cal,padx=22,bd=8, fg="white" ,bg="#919c9a",font=('arial',17),text="9",command=lambda:btnclick(9)).place(x=185,y=155)
mul = Button(cal,padx=16,bd=8, fg="black", bg="#56a4d1",font=('arial',17),text="x",command=lambda:btnclick("*")).place(x=273,y=155)

btn4 = Button(cal,padx=24,bd=8, fg="white" ,bg="#919c9a",font=('arial',17),text="4",command=lambda:btnclick(4)).place(x=5,y=215)
btn5 = Button(cal,padx=22,bd=8, fg="white" ,bg="#919c9a",font=('arial',17),text="5",command=lambda:btnclick(5)).place(x=97,y=215)
btn6 = Button(cal,padx=22,bd=8, fg="white" ,bg="#919c9a",font=('arial',17),text="6",command=lambda:btnclick(6)).place(x=185,y=215)
sub= Button(cal,padx=18,bd=8, fg="black" ,bg="#56a4d1",font=('arial',17),text="-",command=lambda:btnclick("-")).place(x=273,y=215)

btn1 = Button(cal,padx=24,bd=8, fg="white" ,bg="#919c9a",font=('arial',17),text="1",command=lambda:btnclick(1)).place(x=5,y=275)
btn2 = Button(cal,padx=22,bd=8, fg="white" ,bg="#919c9a",font=('arial',17),text="2",command=lambda:btnclick(2)).place(x=97,y=275)
btn3 = Button(cal,padx=22,bd=8, fg="white" ,bg="#919c9a",font=('arial',17),text="3",command=lambda:btnclick(3)).place(x=185,y=275)
Add= Button(cal,padx=16,bd=8, fg="black" ,bg="#56a4d1",font=('arial',17),text="+",command=lambda:btnclick("+")).place(x=273,y=275)

btn0 = Button(cal,padx=68,bd=8, fg="white" ,bg="#919c9a",font=('arial',17),text="0",command=lambda:btnclick(0)).place(x=5,y=335)
btndot = Button(cal,padx=24,bd=8, fg="white" ,bg="#919c9a",font=('arial',17),text=".",command=lambda:btnclick(".")).place(x=185,y=335)
Equal = Button(cal,padx=16,bd=8, fg="black" ,bg="#b7ed6f",font=('arial',17),text="=",command=btneq).place(x=273,y=335)




cal.mainloop()
