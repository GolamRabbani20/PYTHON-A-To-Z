#Python Program to Count the Occurrences of a Word in a Text File
#n=input("Enter file name:")
x=open("data12.txt","r")
m=input("Enter a word:")
c=0
for i in x:
    words=i.split()
    for k in words:
       if k==m:
        c+=1
print(c)