n,k=map(int,input().split())
s=list(map(int,input().strip().split()))
count=0
for i in range(n):
    for j in range(i+1,n):
        if (s[i]+s[j])%k!=0:
            count+=1
print(count)
