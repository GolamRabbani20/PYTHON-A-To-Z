x=[50,45,25,88,12,36,42,14,77,15,10,22,5]
for i in range(1,len(x)):
    temp=x[i]
    k=i-1
    while(k>=0 and x[k]>temp):
        x[k+1]=x[k]
        k-=1
    x[k+1]=temp
print(x)