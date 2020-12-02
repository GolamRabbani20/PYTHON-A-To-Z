x=[]
n,k=input().split()
n=int(n)
k=int(k)
p=input().split()
for i in p:
    x.append(int(i))
count=0
for i in range(n):
    for j in range(1,n):
        if i<j and (x[i]+x[j])%k==0:
            count+=1

print(count)