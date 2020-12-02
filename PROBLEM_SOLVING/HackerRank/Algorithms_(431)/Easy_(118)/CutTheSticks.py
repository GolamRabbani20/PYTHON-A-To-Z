def CutTheSticks(x):
    temp=[]
    while len(x)>0:
        temp.append(len(x))
        x=[i for i in x if i!=min(x)]
    return temp

input()
x=list(map(int,input().strip().split()))
for k in CutTheSticks(x):
    print(k)

