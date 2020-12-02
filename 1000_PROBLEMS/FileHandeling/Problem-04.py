#Python Program to Read a String from the User and Append it into a File
a=input("Enter file name:")
x=open(a,"a")
p=input("Enter a string:")
x.write("\n")
x.write(p)

x=open(a,"r")
#print(x.read())
for k in x:
    print(k,end="")