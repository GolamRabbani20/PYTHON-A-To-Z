n=int(input())
x=list(map(int,input().strip().split()))
Min=1000
for i in range(n):
    for k in range(i+1,n):
        if x[i]==x[k]:
            if abs(i-k)<Min:
                Min=abs(i-k)

if Min==1000:
    print(-1)
else:
    print(Min)