#Python Program to Count the Number of Blank Spaces in a Text File
x=open("data12.txt","r")
c=0
for line in x:
    words=line.split()
    if words==[]:
        pass
    else:
      c=c+len(words)-1
print("\nTotal space =",c)