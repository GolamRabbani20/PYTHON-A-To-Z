def Kangroo(x1,v1,x2,v2):
    if x2>x1 and v2>v1:
        return 0
    else:
        for k in range(10000):
            if k*v1+x1==k*v2+x2:
                return 1
        else:
          return 0

x1,v1,x2,v2=input().split()
x1=int(x1)
x2=int(x2)
v1=int(v1)
v2=int(v2)

if Kangroo(x1,v1,x2,v2)==1:
    print("YES")
else:
    print("NO")