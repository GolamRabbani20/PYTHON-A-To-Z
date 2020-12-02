def QuickSort(x,lb,ub):
    if(lb<ub):
        loc=Partition(x,lb,ub)
        QuickSort(x,lb,loc-1)
        QuickSort(x,loc+1,ub)

def Partition(x,lb,ub):
    Pivot=x[lb]
    start=lb+1
    end=ub
    while start<end:
        while(x[start]<=Pivot):
            start+=1

        while(x[end]>Pivot):
            end-=1
        if start<end:
            temp=x[start]
            x[start]=x[end]
            x[end]=temp

    temp=x[lb]
    x[lb]=x[end]
    x[end]=temp
    return end

x=[7,6,10,5,9,2,1,15,7]
ub=len(x)-1
QuickSort(x,0,ub)
for k in range(ub):
 print(x[k],end=" ")