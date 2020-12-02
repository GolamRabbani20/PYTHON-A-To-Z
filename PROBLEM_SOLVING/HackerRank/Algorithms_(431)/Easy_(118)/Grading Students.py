import math
n=int(input())
x=[]
while n>0:
    x.append(int(input()))
    n=n-1

for k in x:
    p=math.ceil(k/5)*5
    if k>=38:
        if p-k<3:
            print(p)
        else:
            print(k)
    else:
        print(k)