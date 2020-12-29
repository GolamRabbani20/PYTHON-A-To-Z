from tkinter import *
root=Tk()
root.title("Simple Calculator")
e=Entry(root,width=60,borderwidth=4)
e.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

def Click_Button(Number):
    #e.delete(0,END)
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(Number))

def Clear_Button():
    e.delete(0,END)

def Plus_Button():
    first_Num=e.get()
    global f_Num
    global math
    math="addition"
    f_Num=int(first_Num)
    e.delete(0,END)


def Sub_Button():
    first_Num = e.get()
    global f_Num
    global math
    math = "subtraction"
    f_Num = int(first_Num)
    e.delete(0, END)

def Mul_Button():
    first_Num = e.get()
    global f_Num
    global math
    math = "multiplication"
    f_Num = int(first_Num)
    e.delete(0, END)

def Div_Button():
    first_Num = e.get()
    global f_Num
    global math
    math = "division"
    f_Num = int(first_Num)
    e.delete(0, END)

def Equal_Button():
    second_number=e.get()
    e.delete(0,END)
    if math=="addition":
       e.insert(0,f_Num+int(second_number))

    elif math=="subtraction":
        e.insert(0, f_Num - int(second_number))

    elif math=="multiplication":
        e.insert(0, f_Num * int(second_number))

    else:
        e.insert(0, round(f_Num / int(second_number),3))


Button_7=Button(root,text="7",padx=40,pady=20,command=lambda :Click_Button(7)).grid(row=1,column=0)
Button_8=Button(root,text="8",padx=40,pady=20,command=lambda :Click_Button(8)).grid(row=1,column=1)
Button_9=Button(root,text="9",padx=40,pady=20,command=lambda :Click_Button(9)).grid(row=1,column=2)

Button_4=Button(root,text="4",padx=40,pady=20,command=lambda :Click_Button(4)).grid(row=2,column=0)
Button_5=Button(root,text="5",padx=40,pady=20,command=lambda :Click_Button(5)).grid(row=2,column=1)
Button_6=Button(root,text="6",padx=40,pady=20,command=lambda :Click_Button(6)).grid(row=2,column=2)

Button_1=Button(root,text="1",padx=40,pady=20,command=lambda :Click_Button(1)).grid(row=3,column=0)
Button_2=Button(root,text="2",padx=40,pady=20,command=lambda :Click_Button(2)).grid(row=3,column=1)
Button_3=Button(root,text="3",padx=40,pady=20,command=lambda :Click_Button(3)).grid(row=3,column=2)
Button_0=Button(root,text="0",padx=40,pady=20,command=lambda :Click_Button(0)).grid(row=4,column=0)
Button_Point=Button(root,text=".",padx=92,pady=20,command=Sub_Button).grid(row=4,column=1,columnspan=2)

#OPerations
Button_Plus=Button(root,text="+",padx=46,pady=20,command=Plus_Button).grid(row=1,column=3)
Button_Sub=Button(root,text="-",padx=46,pady=20,command=Sub_Button).grid(row=2,column=3)
Button_Mul=Button(root,text="x",padx=46,pady=20,command=Mul_Button).grid(row=3,column=3)
Button_Div=Button(root,text="/",padx=46,pady=20,command=Div_Button).grid(row=4,column=3)
Button_Clear=Button(root,text="Clear",padx=85,pady=20,command=Clear_Button).grid(row=5,column=0,columnspan=2)
Button_Equal=Button(root,text="=",padx=90,pady=20,command=Equal_Button).grid(row=5,column=2,columnspan=2)

root.mainloop()