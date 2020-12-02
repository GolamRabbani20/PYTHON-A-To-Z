from array import *

A=array('i',[])
B=array('i',[])

n,r=input().split()
n=int(n)
r=int(r)
m=n-r
p=0
for i in input().split():
    A.append(int(i))
for k in range(n):
    if k<r:
        B.insert(m,A[k])
        m+=1
    else:
        B.insert(p,A[k])
        p+=1
for e in B:
    print(e,end=" ")
