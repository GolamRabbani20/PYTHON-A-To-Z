from tkinter import*
root=Tk()
def Myclick():
    mylabel=Label(root,text="You have clicked me.")
    mylabel.pack()

mybutton=Button(root,text="Click me",command=Myclick,fg="red",bg="black")
mybutton.pack()
root.mainloop()


"""
state=DISABLE
padx=50
pady=50

color
-------
foreground color fb="red" or "use color code"
Back ground color="black"
"""