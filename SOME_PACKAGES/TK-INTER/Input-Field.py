from tkinter import*
root=Tk()
root.title("Input window")
e=Entry(root,width=50,fg="white",bg="red",borderwidth=5)
e.pack()
e.insert(0,"Enter your name:")
def ClickMe():
    hello="Hello "+e.get()
    mylabel=Label(root,text=hello)
    mylabel.pack()

mybutton=Button(root,text="Show your name",command=ClickMe)
mybutton.pack()
e.mainloop()