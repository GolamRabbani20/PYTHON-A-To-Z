def JumpingOnTheClouds(x,n):
    count=0
    k=0
    while k<n-1:
        k+=(x[k+2]==0)+1
        count+=1
    return count

n=int(input())
x=list(map(int,input().split()))
x.insert(n,0)
print(JumpingOnTheClouds(x,n))