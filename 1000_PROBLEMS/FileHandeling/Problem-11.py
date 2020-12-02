#Python Program to Read a File and Capitalize the First Letter of Every Word in the File
s=input("Enter file name:")
x=open(s,"r")
for line in x:
    k=line.title()
    print(k,end=" ")
