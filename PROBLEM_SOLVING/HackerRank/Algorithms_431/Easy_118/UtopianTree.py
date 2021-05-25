def UtopianTree(n):
    height=1
    if n==0:
        return height
    else:
        for i in range(1,n+1):
            if i%2==1:
                height*=2
            else:
                height+=1
        return height

m=[]
for k in range(int(input())):
    x=int(input())
    m.append(UtopianTree(x))

for r in m:
    print(r)
