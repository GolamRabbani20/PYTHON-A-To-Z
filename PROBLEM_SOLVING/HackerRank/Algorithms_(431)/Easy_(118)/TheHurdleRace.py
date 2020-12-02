def  TheHurdleRace(x,k):
    Max=max(x)
    if k>=Max:
        return 0
    else:
      return abs(Max-k)

n,k=input().split()
k=int(k)
x=list(map(int,input().split()))
print(TheHurdleRace(x,k))