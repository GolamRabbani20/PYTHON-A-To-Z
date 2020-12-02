def MergeSort(x,lb,ub):
    if lb<ub:
        mid=(lb+ub)//2
        MergeSort(x,lb,mid)
        MergeSort(x,mid+1,ub)
        Merge(x,lb,mid,ub)

def Merge(x,lb,mid,ub):
    i=lb
    j=mid+1
    k=lb
    while(i<=lb and j<=ub):
        if x[i]<=x[j]:
            b[k]=x[i]
            i+=1
        else:
            b[k]=x[j]
            j+=1
        k+=1
        if i>mid:
            while(j<=ub):
                b[k]=x[j]
                i+=1
                k+=1
        else:
            while i<=mid:
                b[k]=x[i]
                i+=1
                k+=1
        for k in range(lb,ub):
            x[k]=b[k]
        print(x)

x=[7,6,10,5,9,2,1,15,7]
b=[]
MergeSort(x,0,len(x)-1)