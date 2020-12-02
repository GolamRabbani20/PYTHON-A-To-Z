def ElectronicsShop(x,y,b):
    temp=0
    for k in x:
        for h in y:
            if k+h<=b:
                if temp<k+h:
                    temp=k+h
    return temp

b,n,m=input().split()
b=int(b)
x=list(map(int,input().split()))
y=list(map(int,input().split()))
p=ElectronicsShop(x,y,b)
if p:
    print(p)
else:
    print(-1)
