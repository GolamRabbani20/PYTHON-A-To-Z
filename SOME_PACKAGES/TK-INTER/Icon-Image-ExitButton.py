from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("My window")
root.iconbitmap('C:/ugi/icon.png')
my_img=ImageTk.PhotoImage(Image.open("C:/ugi/lazi.jpg"))
my_label=Label(image=my_img).pack()

Button_Exit=Button(root,text="Close program",command=root.quit).pack()
#Button_Exit1=Button(root,text="Stop!",command=root.destroy).pack()
root.mainloop()