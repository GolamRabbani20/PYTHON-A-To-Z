def HalloweenSale(p,d,m,s):
    count=0
    while s>=p:
        s-=p
        p=max(p-d,m)
        count+=1
    return count

p,d,m,s=input().strip().split()
p,d,m,s=[int(p),int(d),int(m),int(s)]
print(HalloweenSale(p,d,m,s))