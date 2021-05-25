input()
Count=[0]*6
for i in map(int,input().strip().split()):
    Count[i]+=1
print(Count.index(max(Count)))

'''
#Timelimit extends
import array as a
def Migratory_Birds(n,x):
    Max=0
    for i in range(n):
        if x.count(x[i])>Max:
            d=i
            Max=M
    return x[d]

x=a.array('i',[])
n=int(input())
for i in map(int,input().strip().split()):
    x.append(int(i))
print(Migratory_Birds(n,x))'''