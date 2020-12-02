def JumpingOnTheCloudsRevisited(n,k,x):
    Energy=100
    i=k%n
    Energy-=x[i]*2+1
    while i!=0:
        if x[(i+k)%n]:
            Energy-=3
        else:
            Energy-=1
        i=(i+k)%n
    return Energy

n,k=input().split()
n=int(n)
k=int(k)
lst=list(map(int,input().split()))
print(JumpingOnTheCloudsRevisited(n,k,lst))
