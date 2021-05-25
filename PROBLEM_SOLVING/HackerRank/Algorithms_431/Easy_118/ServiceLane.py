def ServiceLane(x,i,j):
    return min(x[i:j+1])

n,t=map(int,input().split())
x=list(map(int,input().split()))
while t:
    i,j=map(int,input().split())
    print(ServiceLane(x,i,j))
    t-=1