#Python Program to Print all the Prime Numbers within a Given Range
m=int(input("Enter lower range:"))
n=int(input("Enter upper range:"))
s=0
x=[]
while m<=n:
    for i in range(2,m):
        if m%i==0:
            s+=1
            break

    if s==0:
        if m==1:
            pass
        else:
         x.append(m)
    else:
       pass
    s=0
    m+=1
print("List of prime:",x)
