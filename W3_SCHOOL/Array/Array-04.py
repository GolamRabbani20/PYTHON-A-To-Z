from array import *
x=array('i',[])
k=0
for _ in input().split():
    x.insert(k,int(_))
    k+=1
i=0
while i is not len(x):
    print(x[i],end=" ")
    i+=1