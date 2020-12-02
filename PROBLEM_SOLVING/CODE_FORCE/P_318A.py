n,k=input().split()
n=int(n)
k=int(k)
n=(n+1)//2
if k>n:
    print(2*(k-n))
else:
    print(2*k-1)