x=open("kamla.txt","r")
#print(x.writable())
print(x.readable())
#z=x.read()
#k=x.readline()[2:20:2]
for i in x:
   print(i,end=" ")
#print(z)
#print(len(z))
x.close()
