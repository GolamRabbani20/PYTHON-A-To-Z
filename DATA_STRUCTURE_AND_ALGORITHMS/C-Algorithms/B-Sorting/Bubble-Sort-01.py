#Normal solution
#x=['a','d','b','m','f']
x=[50,6,35,2,12,5,20,45,0,21]
n=len(x)
for k in range(n-1):
    for i in range(n-1):
        if x[i]>x[i+1]:
            Temp=x[i]
            x[i]=x[i+1]
            x[i+1]=Temp
print(x,end=" ")