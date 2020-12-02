from tkinter import*
from tkinter import messagebox
s=Tk()
def ShowInfo():
    messagebox.showinfo("Hello Python","Hello world")
def ShowError():
    messagebox.showerror("This is going to show error!","Invalid Input!")
def Show_warning():
    messagebox.showwarning("There is a waring!","Never go there.")

B=Button(s,text="Show Info",width=10,command=ShowInfo)
B1=Button(s,text="Show-Error",width=12,command=ShowError)
B2=Button(s,text="Show Warning",width=15,command=Show_warning)
B.pack()
B1.pack()
B2.pack()
s.mainloop()