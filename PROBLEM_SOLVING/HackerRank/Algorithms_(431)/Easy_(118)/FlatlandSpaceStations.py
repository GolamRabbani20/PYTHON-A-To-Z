def FlatlandSpaceStations(n,c):
        c.sort()
        Max=max(c[0], n-1-c[-1])
        for i in range(len(c)-1):
            Max=max((c[i+1]-c[i])//2,Max)
        return Max

n,m=input().strip().split()
n,m=[int(n),int(m)]
c=list(map(int,input().split()))
if n==m:
    print(0)
else:
    print(FlatlandSpaceStations(n,c))