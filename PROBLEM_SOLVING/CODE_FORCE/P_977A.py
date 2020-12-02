n,k=input().split()
k=int(k)
n=int(n)
while k!=0:
    if n%10==0:
        n=n//10
    else:
        n=int(n)-1
    k-=1
print(n)