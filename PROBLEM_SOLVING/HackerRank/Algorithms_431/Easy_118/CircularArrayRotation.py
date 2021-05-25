def CircularArrayRotation(x,k):
    if k>len(x):
        k=k%len(x)
    k=len(x)-k
    x=x[k:]+x[:k]
    return x

n,k,q=input().strip().split()
x=input().strip().split()
h=CircularArrayRotation(x,int(k))
for j in range(int(q)):
    print(h[int(input())])