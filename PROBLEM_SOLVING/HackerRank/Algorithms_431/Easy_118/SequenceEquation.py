'''def SequenceEqation(p):
    for x in range(min(p)+1,max(p)+1):
        y=p.index(p.index(x))
        if p[p[y]]==x:
            print(y)

input()
##p=list(map(int,input().strip().split()))
p=[0]
for i in map(int,input().strip().split()):
    p.append(i)
SequenceEqation(p)
'''

def SequenceEqation(p,n):
    for x in range(1,n+1):
        print(p.index(p.index(x)+1)+1)

n=int(input())
p=list(map(int,input().strip().split()))
SequenceEqation(p,n)