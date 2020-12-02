#Python Program to Count the Number of Lines in a Text File
s=input("Enter name of file:")
x=open(s,"r")
line=0
for i in x:
    line+=1
print("Number of lines:",line)