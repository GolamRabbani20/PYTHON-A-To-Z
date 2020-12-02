#Most optiml/efficient solution
#x=[50,6,35,2,12,5,20,45,0,21]
#x=['a','d','b','m','f']
x=[]
p=input("Enter element:").split()
for k in p:
    x.append(int(k))
n=len(x)
for k in range(n-1):
    flag=0
    for i in range(n-1-k):
        if x[i]>x[i+1]:
            Temp=x[i]
            x[i]=x[i+1]
            x[i+1]=Temp
            flag=1
    if flag==0:
       break
print(x,end=" ")