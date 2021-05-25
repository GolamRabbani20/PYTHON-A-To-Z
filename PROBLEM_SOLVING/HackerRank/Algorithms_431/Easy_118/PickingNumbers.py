def PickingNumbers(x):
    Max=0
    for k in x:
        m=x.count(k)+x.count(k+1) #x.count(k)+x.count(k-1)
        if m>Max:
            Max=m
    return Max

n=int(input())
x=list(map(int,input().strip().split()))
print(PickingNumbers(x))
