x=[50,45,25,88,12,36,42,14,77,15,10,22,5]
for i in range(len(x)-1):
    min=i
    for k in range(i+1,len(x)):
        if x[k]<x[min]:
            min=k
    if min!=i:
        temp=x[i]
        x[i]=x[min]
        x[min]=temp
print(x)