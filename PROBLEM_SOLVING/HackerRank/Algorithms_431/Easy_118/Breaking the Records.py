def BreakingTheRecords(n,x):
    MaxScore=0
    MinScore=0
    Max=x[0]
    Min=x[0]
    for k in range(n-1):
        if x[k+1]<Min:
            Min=x[k+1]
            MinScore+=1
        elif x[k+1]>Max:
            Max=x[k+1]
            MaxScore+=1
    print(MaxScore,MinScore)

x=[]
n=int(input())
P=input().split()
for i in P:
    x.append(int(i))

BreakingTheRecords(n,x)