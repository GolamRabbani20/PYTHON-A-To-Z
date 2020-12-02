from array import *
x=array('i',[2,42,5,6,65,6,6,63])
#k=input("Enter values:").split()
#for i in x:
    #x.append(int(i))
#print(x.buffer_info())  #address and size print korbe
#x.insert(2,500)
#print(x.index(500))
#x.reverse()
#print(x.count(6))
#print(len(x))
#x.pop()
#x.pop()
#x.remove(65)


new=array(x.typecode,(a*a for a in x))
for r in new:
    print(r,end=" ")
print()

p=0
while(p<len(x)):
    print(x[p],end=" ")
    p+=1
